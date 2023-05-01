import os,time,sys
import pymem

process_name = "EverStopped-Win64-Shipping.exe"

offset_base = 0x7ff7dd8a0000

def main():
	global pm
	pm = pymem.Pymem(process_name)

	offset_localplayer = get_offset(pm, offset_base, 0x42D33C8, 0x88, 0x240, 0x74)
	offset_ammo = offset_localplayer + 0x498
	offset_crouch = offset_localplayer + 0x4F0
	offset_light = offset_localplayer + 0x4EC

	offset_cases = get_offset(pm, offset_base, 0x4363978, 0x8, 0x1D8, 0x28)
	offset_frag = offset_cases + 0x18

	offset_points = get_offset(pm, offset_base, 0x4363978, 0x0, 0x198, 0x1B0)

	offset_death = get_offset(pm, offset_base, 0x4368100, 0x118, 0x2F0, 0x1F8, 0x50)

	print("LocalPlayer : " + hex(offset_localplayer))

	print("\nAmmo : "+hex(offset_ammo))
	print("Crouch Time : "+hex(offset_crouch))
	print("Light Time : "+hex(offset_light))

	print("\nCases : "+hex(offset_cases))
	print("Fragements: "+hex(offset_frag))

	print("\nPoints : "+hex(offset_points))

	print("\nDeath : "+hex(offset_death))
	return

def get_offset(mem, base, *ptrs):
	if not ptrs:
		return None

	offset_ptr = base + ptrs[0]

	for ptr in ptrs[1:]:
		offset_ptr = mem.read_ulonglong(offset_ptr) + ptr

	return offset_ptr

if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"Error : {e}")
		sys.exit()