from classes import *
import multi

# Initialize
actionList = []
groupList = []
equipmentList = []
equipmentSlotList = []

## Key to reset all countdowns
resetKey = '-'

## Key to change Arcs when mounted
mountKey = '+'

## Add your tracked actions here
actionList.append(TrackedAction('Heal',ColorCode.LBLUE,[CooldownGroup.NONE],ActionType.ATKREGULAR,['1','2','F1'],1.1,visible=False,ap=ArcPlacement.LEFT))
actionList.append(TrackedAction('Attack',ColorCode.RED,[CooldownGroup.NONE],ActionType.ATKREGULAR,['6','7','8','9','Q','`'],2.1,visible=False,ap=ArcPlacement.RIGHT))
actionList.append(TrackedAction('Attack',ColorCode.RED,[CooldownGroup.NONE],ActionType.ATKREGULAR,['F7'],4.1,visible=False,ap=ArcPlacement.RIGHT))

actionList.append(TrackedAction('Potion',ColorCode.PINK,[CooldownGroup.NONE],ActionType.ATKREGULAR,['3','4'],1.1,visible=False,ap=ArcPlacement.RIGHT))
actionList.append(TrackedAction('Utito Tempo',ColorCode.RED,[CooldownGroup.NONE],ActionType.ATKREGULAR,['0'],11.5,visible=False,ap=ArcPlacement.LEFT))

actionList.append(TrackedAction('Exura',ColorCode.LBLUE,[CooldownGroup.NONE],ActionType.ATKREGULAR,['1'],1.1,visible=True))
actionList.append(TrackedAction('Exura Gran',ColorCode.LBLUE,[CooldownGroup.NONE],ActionType.ATKREGULAR,['2'],600.1,visible=True))
actionList.append(TrackedAction('Utura',ColorCode.LBLUE,[CooldownGroup.NONE],ActionType.ATKREGULAR,['F1'],60.1,visible=True))


actionList.append(TrackedAction('Exori',ColorCode.RED,[CooldownGroup.NONE],ActionType.ATKREGULAR,['7'],4.1,visible=True))
actionList.append(TrackedAction('ExoriGran',ColorCode.RED,[CooldownGroup.NONE],ActionType.ATKREGULAR,['8'],6.1,visible=True))
actionList.append(TrackedAction('ExoriMin',ColorCode.RED,[CooldownGroup.NONE],ActionType.ATKREGULAR,['9'],6.1,visible=True))
actionList.append(TrackedAction('ExoriMas',ColorCode.RED,[CooldownGroup.NONE],ActionType.ATKREGULAR,['Q'],8.1,visible=True))

actionList.append(TrackedAction('ExoriHur',ColorCode.WHITE,[CooldownGroup.NONE],ActionType.ATKREGULAR,['6'],6.1,visible=True))
actionList.append(TrackedAction('ExoriGran',ColorCode.WHITE,[CooldownGroup.NONE],ActionType.ATKREGULAR,['F7'],30.1,visible=True))
actionList.append(TrackedAction('ExoriIco',ColorCode.WHITE,[CooldownGroup.NONE],ActionType.ATKREGULAR,['`'],6.1,visible=True))

actionList.append(TrackedAction('Haste',ColorCode.GRAY,[CooldownGroup.NONE],ActionType.SUPPORTEFFECT,['E'],31.0))

# actionList.append(TrackedAction('Rune',ColorCode.rgb2hex((255,100,0)),[CooldownGroup.ATTACK,CooldownGroup.OBJECT],ActionType.ATKRUNE,[']'],ut=UseType.CROSSHAIR,visible=False))
actionList.append(TrackedAction('GFB',ColorCode.RED,[CooldownGroup.NONE],ActionType.ATKRUNE,['G'],visible=True))
actionList.append(TrackedAction('FireWall',ColorCode.RED,[CooldownGroup.NONE],ActionType.ATKRUNE,['J'],ut=UseType.CROSSHAIR,visible=True))
# actionList.append(TrackedAction('FireBomb',ColorCode.RED,[CooldownGroup.ATTACK,CooldownGroup.OBJECT],ActionType.ATKRUNE,['shift+@'],ut=UseType.CROSSHAIR,visible=False))

# Attack Spells
# actionList.append(TrackedAction('StrongIce',ColorCode.rgb2hex((0,150,255)),[CooldownGroup.ATTACK,CooldownGroup.STRONGSTRIKE],ActionType.ATKCOOLDOWN,['shift+{'],8.0,visible=False))
# actionList.append(TrackedAction('StrongTerra',ColorCode.rgb2hex((0,255,137)),[CooldownGroup.ATTACK,CooldownGroup.STRONGSTRIKE],ActionType.ATKCOOLDOWN,['F9'],8.0,visible=False))

# actionList.append(TrackedAction('IceWave',ColorCode.rgb2hex((0,150,255)),[CooldownGroup.ATTACK],ActionType.ATKCOOLDOWN,['shift+}'],8.0,visible=True))
# actionList.append(TrackedAction('TerraWave',ColorCode.rgb2hex((0,255,137)),[CooldownGroup.ATTACK],ActionType.ATKCOOLDOWN,['F10'],4.0,visible=True))

# actionList.append(TrackedAction('UltimateIce',ColorCode.rgb2hex((0,150,255)),[CooldownGroup.ATTACK,CooldownGroup.SPECIAL],ActionType.ATKCOOLDOWN,['F11'],30.0))
#actionList.append(TrackedAction('UltimateTerra',ColorCode.rgb2hex((0,137,255)),[CooldownGroup.ATTACK,CooldownGroup.SPECIAL],ActionType.ATKCOOLDOWN,['F11'],30.0))

# actionList.append(TrackedAction('Ice UE',ColorCode.ORANGE,[CooldownGroup.ATTACK,CooldownGroup.SPECIAL],ActionType.ATKCOOLDOWN,['F12'],40.0))
#actionList.append(TrackedAction('Terra UE',ColorCode.ORANGE,[CooldownGroup.ATTACK,CooldownGroup.SPECIAL],ActionType.ATKCOOLDOWN,['F12'],40.0))

# Heal
# actionList.append(TrackedAction('Exura',ColorCode.LBLUE,[CooldownGroup.HEAL],ActionType.HEALREGULAR,['3'],visible=False,ap=ArcPlacement.LEFT))
# actionList.append(TrackedAction('Exura Gran',ColorCode.LBLUE,[CooldownGroup.HEAL],ActionType.HEALREGULAR,['2'],visible=False))

# Support
#actionList.append(TrackedAction('Magic Shield',ColorCode.WHITE,[CooldownGroup.SUPPORT],ActionType.SUPPORTEFFECT,['4'],200.0))
# actionList.append(TrackedAction('MWall',ColorCode.RED,[CooldownGroup.SUPPORT,CooldownGroup.OBJECT],ActionType.ATKRUNE,['shift+#'],ut=UseType.CROSSHAIR,visible=False))

## Equipment to be tracked
# Rings
# equipmentList.append(TrackedEquipment('LifeRing', ColorCode.DGREEN,[CooldownGroup.NONE],ActionType.EQUIPMENT,['F2'],1200.0,et=EquipmentType.RING))
# equipmentList.append(TrackedEquipment('RingHealing', ColorCode.rgb2hex((227,115,32)),[CooldownGroup.NONE],ActionType.EQUIPMENT,['F3'],450.0,et=EquipmentType.RING))
# equipmentList.append(TrackedEquipment('SwordR', ColorCode.ORANGE,[CooldownGroup.NONE],ActionType.EQUIPMENT,['5'],1800.0,iv=355.0,et=EquipmentType.RING))
# equipmentList.append(TrackedEquipment('PrismaR', ColorCode.BLUE,[CooldownGroup.NONE],ActionType.EQUIPMENT,['F3'],1800.0,iv=355.0,et=EquipmentType.RING))

## DO NOT DELETE GROUPS. IF YOU DONT WANT TO SEE IT, JUST SET 'visible=False' IN ARGUMENTS
groupList.append(TrackedGroup('Potion',ColorCode.PINK,CooldownGroup.OBJECT,1.0,visible=False))
groupList.append(TrackedGroup('Attack',ColorCode.RED,CooldownGroup.ATTACK,2.0,visible=False))
groupList.append(TrackedGroup('Healing',ColorCode.LBLUE,CooldownGroup.HEAL,1.0,visible=False))
groupList.append(TrackedGroup('Support',ColorCode.DGREEN,CooldownGroup.SUPPORT,2.0,visible=False))
groupList.append(TrackedGroup('Conjure',ColorCode.BLACK,CooldownGroup.CONJURE,2.0,visible=False))
groupList.append(TrackedGroup('Special',ColorCode.ORANGE,CooldownGroup.SPECIAL,4.0,visible=False))
groupList.append(TrackedGroup('StrongStrike',ColorCode.rgb2hex((0,150,255)),CooldownGroup.STRONGSTRIKE,8.0,visible=False))

## DO NOT DELETE EQUIPMENT SLOTS
equipmentSlotList.append(TrackedEquipmentSlot(EquipmentType.RING))
equipmentSlotList.append(TrackedEquipmentSlot(EquipmentType.BOOTS))
equipmentSlotList.append(TrackedEquipmentSlot(EquipmentType.WEAPON))
equipmentSlotList.append(TrackedEquipmentSlot(EquipmentType.HELMET))
equipmentSlotList.append(TrackedEquipmentSlot(EquipmentType.SHIELD))
equipmentSlotList.append(TrackedEquipmentSlot(EquipmentType.ARMOR))
equipmentSlotList.append(TrackedEquipmentSlot(EquipmentType.LEGS))

# Separators for the tracked actions section
emptyLines = [4,8,11];

def debugMode():
	print('Debug Mode: press hotkeys to see how to add them in the script')
	while(True):
		s = keyboard.read_hotkey(suppress=False)
		print(s)

def main(options):
	# Checks for setup  flag
	if len(options) > 1:			
		if options[1] == "setup": 
			print("Starting in setup mode.")
			setup = True
	else:
		setup = False

	# Create position handler
	positionHandler = PositionHandler()

	# Create transparent window
	windowHandler = WindowHandler(actionList,groupList,equipmentList,emptyLines, positionHandler)

	# Thread that detects keyboard hotkeys
	tHotkeyTracker = HotkeyTracker(actionList,equipmentList,groupList,windowHandler,positionHandler,resetKey,mountKey)

	# Thread that detects mouse buttons
	tMouseTracker = MouseTracker(actionList,positionHandler)

	# Thread that tracks actions
	tActionTracker = ActionTracker(actionList,equipmentList,groupList,equipmentSlotList)
	
	# Setup mode
	if setup:
		windowHandler.setupMode()
		tMouseTracker.setupMode()
		tHotkeyTracker.setupMode()
		tActionTracker.setupMode()

	# Start threads
	tMouseTracker.start()
	tHotkeyTracker.start()
	tActionTracker.start()

	try:
		while(True):
			win32gui.RedrawWindow(windowHandler.hWindow, None, None, win32con.RDW_INVALIDATE | win32con.RDW_ERASE)
			win32gui.PumpWaitingMessages()
			time.sleep(0.05)
		
	except KeyboardInterrupt:
		print("\nScript interrupted")
				
		tActionTracker.abort = True
		tActionTracker.join()
		print("Action Tracker Stopped")
		
		tMouseTracker.join()
		print("Mouse Tracker Stopped")
		
		tHotkeyTracker.join()	
		print("Hotkey Tracker Stopped")

		win32gui.DestroyWindow(windowHandler.hWindow)
		print("Overlay window destroyed")
		print("Closing...")	

if __name__ == '__main__':
	main(sys.argv)
