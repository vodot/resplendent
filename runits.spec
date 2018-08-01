
[spec]

; Format and options of this spec file:
options = "+spec3"

[info]

; Apolyton Tileset created by CapTVK with thanks to the Apolyton Civ2
; Scenario League.

; Special thanks go to:
; Alex Mor and Captain Nemo for their excellent graphics work
; in the scenarios 2194 days war, Red Front, 2nd front and other misc graphics. 
; Fairline for his huge collection of original Civ2 unit spanning centuries
; Bebro for his collection of mediveal units and ships

artists = "
    Alex Mor [Alex]
    Allard H.S. Höfelt [AHS]
    Bebro [BB]
    Captain Nemo [Nemo][MHN]
    CapTVK [CT] <thomas@worldonline.nl>
    Curt Sibling [CS]
    Erwan [EW]
    Fairline [GB]
    GoPostal [GP]
    Oprisan Sorin [Sor]
    Tanelorn [T]
    Paul Klein Lankhorst / GukGuk [GG]
    Andrew ''Panda´´ Livings [APL]
    Vodvakov
    J. W. Bjerk / Eleazar <www.jwbjerk.com>
    qwm
    FiftyNine
"

[file]
gfx = "ngmod/units"

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 64
dy = 48

tiles = { "row", "column", "tag"
				; Scenario League tags in brackets
  0,  0, "u.armor2"		
  0,  1, "u.howitzer"		
  0,  2, "u.dreadnaught"		
  0,  3, "u.bomber"		
  0,  4, "u.mortar"		
  0,  5, "u.caravan"		
  0,  6, "u.carrier"		
  0,  7, "u.catapult"		
  0,  8, "u.rider"		
  0,  9, "u.chariot2"		
  0, 10, "u.aegis_cruiser"	
  0, 11, "u.diplomat9"		
  0, 12, "u.fighter"		
  0, 13, "u.lightcar"		
  0, 14, "u.ironclad"		
  0, 15, "u.knights"		
  0, 16, "u.legion"		
  0, 17, "u.modfrigate"		
  0, 18, "u.footsold"		
  0, 19, "u.musketeers"		
  1,  0, "u.nuclear"		
  1,  1, "u.phalanx"		
  1,  2, "u.riflemen9"		
  1,  3, "u.viking"		
  1,  4, "u.pioneers"		
  1,  5, "u.submarine"		
  1,  6, "u.merchantman"      
  1,  7, "u.galley2"		
  1,  8, "u.bowmen2"		
  1,  9, "u.mountdrag"		
  1, 10, "u.cruise_missile"	
  1, 11, "u.destroyer"		
  1, 12, "u.dragoons"		
  1, 13, "u.explorer"		
  1, 14, "u.freight"		
  1, 15, "u.galleon"		
  1, 16, "u.partisan"		
  1, 17, "u.pikemen"		
  1, 18, "u.mech_inf"        
  1, 19, "u.rocket_artillery" 
  2,  0, "u.specops2"		
  2,  1, "u.spy"		
  2,  2, "u.engineers"		
  2,  3, "u.heavycannon"		
  2,  4, "u.comanche"		
  2,  5, "u.alpine_troops"	
  2,  6, "u.stealth_bomber"	
  2,  7, "u.strikefighter"	
  2,  8, "u.ptboat"	      
  2,  9, "u.paratroopers"	
  2, 10, "u.elephants"		
  2, 11, "u.crusaders"		
  2, 12, "u.fanatics"		
  2, 13, "u.awacs"		
  2, 14, "u.worker"		
  2, 15, "u.leader"		
  2, 16, "u.barbarian_leader"	
  2, 17, "u.peasants"		
  2, 18, "u.tank"
  2, 19, "u.helicopter"
 

  

; Veteran Levels: up to 9 military honors for experienced units

  3, 0, "unit.vet_1"
  3, 1, "unit.vet_2"
  3, 2, "unit.vet_3"
  3, 3, "unit.vet_4"
  3, 4, "unit.vet_5"
  3, 5, "unit.vet_6"
  3, 6, "unit.vet_7"
  3, 7, "unit.vet_8"
  3, 8, "unit.vet_9"
  
  3, 10, "u.frigate"
  3, 11, "unit.lowfuel"
  3, 11, "unit.tired"


  3, 14, "u.mounted"
  3, 15, "u.raiders"	
  3, 16, "u.uboat"
  3, 17, "u.halftrack"
  3, 18, "u.uav"
; 3, 19, "u.civ_war"
  4, 0,  "u.keshik"
  
  4, 2,  "u.cavalries"
  4, 3,  "u.horsemen"
  4, 4,  "u.warriors"
  4, 5,  "u.transport"
  4, 6,  "u.riflemen"

  4, 8,  "u.trireme"
  4, 9,  "u.galley"
  4, 10, "u.caravel"
  4, 11, "u.cavalry"
  4, 12, "u.agent"
  4, 15, "u.battleship"
  4, 17, "u.nomads" 
  5,  0, "u.cannon3"
  5,  1, "u.infantry"		
  5,  2, "u.carrack"		
  5,  3, "u.canoes9"		
  5,  4, "u.impi"		
  5,  5, "u.jaguar"		
  5,  6, "u.archers"      
  5,  7, "u.axemen"		
  5,  8, "u.chariot"		
  5,  9, "u.spartans"		
  5, 10, "u.jetbomber"	
  5, 11, "u.jetfighter"		
  5, 12, "u.airship"		
  5, 13, "u.artillery4"		
  5, 14, "u.bibomber"		
  5, 15, "u.bifighter"		
  5, 16, "u.stealth_fighter"		
  5, 17, "u.cruiser"		
  5, 18, "u.abrams"        
  5, 19, "u.aaa"
  6,  0, "u.tracked_artillery" 
  6,  1, "u.radar_artillery"
  6,  2, "u.gunship"
  6,  3, "u.modern_infantry"
  6,  4, "u.civilian" 
  6,  5, "u.general"
  6,  6, "u.anti_tank"
  6,  7, "u.armor"
  6,  8, "u.bradley"
  6,  9, "u.m113"
  6, 10, "u.humvee"
  6, 11, "u.assault"
  6, 12, "u.wwiiarmor"
  6, 13, "u.wwiiarty"
  6, 14, "u.grenadiers"
  6, 15, "u.wwiinfantry"
  6, 16, "u.specialists"
  6, 17, "u.machinegun"
  6, 18, "u.marines"
  6, 19, "u.saboteur"
  7, 0,  "u.prophet"
  7, 1,  "u.nucbmr"
  7, 2,  "u.scientist"
  7, 3,  "u.guerilla"
  7, 4,  "u.specops"
  7, 5,  "u.surveyors"
  7, 7,  "u.peltast"
  7, 8,  "u.artillery"
  7, 9,  "u.merchant"
  7, 10, "u.cannon"
  7, 11, "u.philosopher"
  7, 12, "u.envoy"
  7, 13, "u.peon"
  7, 14, "u.expedition"
  7, 15, "u.bowmen"
  7, 16, "u.pikes"
  7, 17, "u.settlers"
  7, 18, "u.midinfantry"
  7, 19, "u.raptor"
  8, 0,  "u.industrialist"
  8, 1,  "u.diplomat"
  8, 2,  "u.3"
  8, 3,  "u.4"
  8, 4,  "u.5"
  8, 5,  "u.6"
  8, 7,  "u.7"
  8, 8,  "u.8"
  8, 9,  "u.9"
  8, 10, "u.10"
  8, 11, "u.11"
  8, 12, "u.12"
  8, 13, "u.13"
  8, 14, "u.14"
  8, 15, "u.15"
  8, 16, "u.16"
  8, 17, "u.17"
  8, 18, "u.18"
  8, 19, "u.19"  
}
