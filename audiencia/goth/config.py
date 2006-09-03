import os
#"0"	"id"
#"1"	"imageName"
#"2"	"category"
#"3"	"layer"
#"4"	"snapPosX"
#"5"	"snapPosY"
#"6" "wearing"
#"7" "waldrobe"

items = ID, ImageName, Category, Layer, SnapPosX, SnapPosY, Wearing, Waldrobe \
    = range(8)

#from wget http://www.stortroopers.com/classic_boy/data/articles.php
configdata = """ "721" "girl_dress_01.gif" "tops" "tops n bottoms" "31" "68" "-1"
"722" "girl_dress_02.gif" "tops" "tops n bottoms" "30" "69" "-1"
"723" "girl_dress_03.gif" "tops" "tops n bottoms" "38" "69" "-1"
"724" "girl_dress_04.gif" "tops" "tops n bottoms" "24" "61" "-1"
"725" "girl_dress_05.gif" "tops" "tops n bottoms" "4" "70" "-1"
"726" "girl_hair_00.gif" "hair" "hair" "27" "25" "-1"
"727" "girl_hair_01.gif" "hair" "hair" "27" "24" "-1"
"728" "girl_hair_02.gif" "hair" "hair" "27" "24" "-1"
"729" "girl_hair_03.gif" "hair" "hair" "27" "24" "-1"
"730" "girl_hair_04.gif" "hair" "hair" "34" "15" "-1"
"731" "girl_hair_05.gif" "hair" "hair" "20" "20" "-1"
"732" "girl_hair_07.gif" "hair" "hair" "31" "19" "-1"
"733" "girl_hair_08.gif" "hair" "hair" "16" "16" "-1"
"734" "girl_hair_09.gif" "hair" "hair" "30" "26" "-1"
"735" "girl_hair_10.gif" "hair" "hair" "28" "27" "-1"
"736" "girl_hair_12.gif" "hair" "hair" "25" "25" "-1"
"737" "girl_hair_14.gif" "hair" "hair" "19" "23" "-1"
"738" "girl_hair_15.gif" "hair" "hair" "29" "19" "-1"
"739" "girl_hair_16.gif" "hair" "hair" "28" "23" "-1"
"740" "girl_hair_18.gif" "hair" "hair" "17" "16" "-1"
"741" "girl_hair_19.gif" "hair" "hair" "27" "16" "-1"
"742" "girl_hair_20.gif" "hair" "hair" "28" "16" "-1"
"743" "girl_hair_21.gif" "hair" "hair" "28" "27" "-1"
"744" "girl_hair_22.gif" "hair" "hair" "32" "26" "-1"
"745" "girl_hair_23.gif" "hair" "hair" "32" "26" "-1"
"746" "girl_hair_24.gif" "hair" "hair" "28" "26" "-1"
"747" "girl_hair_25.gif" "hair" "hair" "32" "5" "-1"
"748" "girl_hair_26.gif" "hair" "hair" "20" "5" "-1"
"749" "girl_hair_27.gif" "hair" "hair" "30" "13" "-1"
"750" "girl_hair_28.gif" "hair" "hair" "20" "18" "-1"
"751" "girl_jumper_01.gif" "tops" "tops n bottoms" "27" "66" "-1"
"752" "girl_jumper_02.gif" "tops" "tops n bottoms" "27" "70" "-1"
"753" "girl_makeup_01.gif" "pants" "underware" "35" "40" "-1"
"754" "girl_makeup_02.gif" "pants" "underware" "36" "44" "-1"
"755" "girl_makeup_03.gif" "pants" "underware" "37" "42" "-1"
"756" "girl_makeup_04.gif" "pants" "underware" "35" "44" "-1"
"757" "girl_makeup_05.gif" "pants" "underware" "36" "39" "-1"
"758" "girl_makeup_06.gif" "pants" "underware" "36" "42" "-1"
"759" "girl_makeup_07.gif" "pants" "underware" "36" "41" "-1"
"760" "girl_makeup_08.gif" "pants" "underware" "36" "43" "-1"
"761" "girl_makeup_09.gif" "pants" "underware" "36" "44" "-1"
"762" "girl_mask_01.gif" "hats" "hats" "31" "40" "-1"
"763" "girl_pants_00.gif" "pants" "underware" "26" "70" "-1"
"764" "girl_pants_01.gif" "pants" "underware" "26" "73" "-1"
"765" "girl_pants_02.gif" "pants" "underware" "36" "72" "-1"
"766" "girl_pants_04.gif" "pants" "underware" "42" "96" "-1"
"767" "girl_pants_05.gif" "pants" "underware" "41" "83" "-1"
"768" "girl_pants_06.gif" "pants" "underware" "44" "96" "-1"
"769" "girl_pants_07.gif" "pants" "underware" "40" "69" "-1"
"770" "girl_pants_08.gif" "pants" "underware" "37" "106" "-1"
"771" "girl_pants_09.gif" "pants" "underware" "40" "68" "-1"
"772" "girl_rubber_01.gif" "tops" "tops n bottoms" "27" "67" "-1"
"773" "girl_shirt_01.gif" "tops" "tops n bottoms" "26" "69" "-1"
"774" "girl_shoes_01.gif" "shoes" "shoes" "34" "91" "-1"
"775" "girl_shoes_02.gif" "shoes" "shoes" "37" "118" "-1"
"776" "girl_shoes_03.gif" "shoes" "shoes" "36" "129" "-1"
"777" "girl_shoes_04.gif" "shoes" "shoes" "36" "119" "-1"
"778" "girl_shoes_05.gif" "shoes" "shoes" "37" "111" "-1"
"779" "girl_skirt_02.gif" "bottoms" "tops n bottoms" "39" "94" "-1"
"780" "girl_skirt_03.gif" "bottoms" "tops n bottoms" "40" "94" "-1"
"781" "girl_skirt_04.gif" "bottoms" "tops n bottoms" "40" "94" "-1"
"782" "girl_skirt_05.gif" "bottoms" "tops n bottoms" "38" "96" "-1"
"783" "girl_top_01.gif" "tops" "tops n bottoms" "27" "70" "-1"
"784" "girl_top_02.gif" "tops" "tops n bottoms" "39" "76" "-1"
"785" "girl_top_03.gif" "tops" "tops n bottoms" "39" "75" "-1"
"786" "girl_top_04.gif" "tops" "tops n bottoms" "39" "70" "-1"
"787" "girl_top_05.gif" "tops" "tops n bottoms" "38" "70" "-1"
"788" "girl_top_06.gif" "tops" "tops n bottoms" "41" "68" "-1"
"789" "girl_top_07.gif" "tops" "tops n bottoms" "32" "70" "-1"
"790" "girl_top_08.gif" "tops" "tops n bottoms" "33" "70" "-1"
"791" "girl_top_09.gif" "tops" "tops n bottoms" "28" "70" "-1"
"792" "girl_top_10.gif" "tops" "tops n bottoms" "40" "70" "-1"
"793" "girl_top_11.gif" "tops" "tops n bottoms" "39" "71" "-1"
"794" "girl_top_12.gif" "tops" "tops n bottoms" "40" "78" "-1"
"795" "girl_trouser_01.gif" "bottoms" "tops n bottoms" "38" "94" "-1"
"796" "girl_trouser_02.gif" "bottoms" "tops n bottoms" "39" "95" "-1"
"797" "girl_trouser_03.gif" "bottoms" "tops n bottoms" "39" "97" "-1"
"798" "boy_body_01.gif" "body" "body" "26" "28" "-1"
"799" "boy_body_02.gif" "body" "body" "26" "28" "-1"
"800" "boy_body_03.gif" "body" "body" "26" "28" "-1"
"801" "girl_body04.gif" "body" "body" "27" "28" "-1"
"802" "girl_body_01.gif" "body" "body" "27" "28" "-1"
"803" "girl_body_02.gif" "body" "body" "27" "28" "-1"
"804" "girl_body_03.gif" "body" "body" "27" "28" "-1"
"805" "boy_trousers_01.gif" "bottoms" "tops n bottoms" "37" "99" "-1"
"806" "boy_trousers_02.gif" "bottoms" "tops n bottoms" "39" "94" "-1"
"807" "boy_trousers_03.gif" "bottoms" "tops n bottoms" "38" "95" "-1"
"808" "boy_trousers_04.gif" "bottoms" "tops n bottoms" "37" "98" "-1"
"809" "boy_trousers_05.gif" "bottoms" "tops n bottoms" "39" "99" "-1"
"810" "boy_trousers_06.gif" "bottoms" "tops n bottoms" "32" "84" "-1"
"811" "boy_trousers_07.gif" "bottoms" "tops n bottoms" "39" "92" "-1"
"812" "girl_skirt_01.gif" "bottoms" "tops n bottoms" "38" "99" "-1"
"813" "girl_trousers_04.gif" "bottoms" "tops n bottoms" "39" "96" "-1"
"814" "girl_trousers_05.gif" "bottoms" "tops n bottoms" "33" "97" "-1"
"815" "girl_trousers_06.gif" "bottoms" "tops n bottoms" "39" "97" "-1"
"816" "girl_trousers_07.gif" "bottoms" "tops n bottoms" "39" "97" "-1"
"817" "girl_trousers_08.gif" "bottoms" "tops n bottoms" "38" "96" "-1"
"818" "boy_facialhair_02.gif" "hair" "hair" "43" "57" "-1"
"819" "boy_facialhair_03.gif" "hair" "hair" "35" "56" "-1"
"820" "boy_hair_01.gif" "hair" "hair" "31" "18" "-1"
"821" "boy_hair_02.gif" "hair" "hair" "33" "18" "-1"
"822" "boy_hair_03.gif" "hair" "hair" "31" "17" "-1"
"823" "boy_hair_04.gif" "hair" "hair" "33" "22" "-1"
"824" "boy_hair_05.gif" "hair" "hair" "31" "19" "-1"
"825" "boy_hair_06.gif" "hair" "hair" "31" "16" "-1"
"826" "boy_hair_07.gif" "hair" "hair" "29" "12" "-1"
"827" "boy_hair_08.gif" "hair" "hair" "32" "28" "-1"
"828" "boy_hair_09.gif" "hair" "hair" "36" "21" "-1"
"829" "boy_hair_10.gif" "hair" "hair" "23" "16" "-1"
"830" "boy_hair_11.gif" "hair" "hair" "32" "26" "-1"
"831" "boy_hair_12.gif" "hair" "hair" "33" "26" "-1"
"832" "boy_hair_13.gif" "hair" "hair" "35" "28" "-1"
"833" "boy_hair_14.gif" "hair" "hair" "26" "19" "-1"
"834" "boy_hair_15.gif" "hair" "hair" "31" "26" "-1"
"835" "boy_hair_16.gif" "hair" "hair" "29" "20" "-1"
"836" "boy_makeup_01.gif" "pants" "underware" "36" "36" "-1"
"837" "boy_makeup_02.gif" "pants" "underware" "35" "45" "-1"
"838" "boy_makeup_03.gif" "pants" "underware" "35" "37" "-1"
"839" "boy_makeup_04.gif" "pants" "underware" "38" "47" "-1"
"840" "boy_makeup_05.gif" "pants" "underware" "36" "45" "-1"
"841" "boy_makeup_06.gif" "pants" "underware" "39" "47" "-1"
"842" "boy_pants_01.gif" "pants" "underware" "40" "94" "-1"
"843" "boy_pants_02.gif" "pants" "underware" "39" "95" "-1"
"844" "boy_pants_03.gif" "pants" "underware" "41" "68" "-1"
"845" "boy_pants_04.gif" "pants" "underware" "40" "94" "-1"
"846" "boy_shoes_01.gif" "shoes" "shoes" "36" "131" "-1"
"847" "boy_shoes_02.gif" "shoes" "shoes" "36" "125" "-1"
"848" "boy_shoes_03.gif" "shoes" "shoes" "37" "119" "-1"
"849" "boy_shoes_04.gif" "shoes" "shoes" "37" "119" "-1"
"850" "boy_shoes_05.gif" "shoes" "shoes" "37" "97" "-1"
"851" "boy_shoes_06.gif" "shoes" "shoes" "37" "118" "-1"
"852" "boy_coat_01.gif" "tops" "jackets" "25" "62" "-1"
"853" "boy_coat_04.gif" "tops" "jackets" "25" "66" "-1"
"854" "boy_shirt_07.gif" "tops" "tops n bottoms" "28" "68" "-1"
"855" "boy_shirt_08.gif" "tops" "tops n bottoms" "26" "67" "-1"
"856" "boy_tee_01.gif" "tops" "tops n bottoms" "39" "70" "-1"
"857" "boy_tee_02.gif" "tops" "tops n bottoms" "31" "70" "-1"
"858" "boy_tee_03.gif" "tops" "tops n bottoms" "32" "70" "-1"
"859" "boy_tee_04.gif" "tops" "tops n bottoms" "31" "70" "-1"
"860" "boy_tee_05.gif" "tops" "tops n bottoms" "31" "70" "-1"
"861" "boy_tee_06.gif" "tops" "tops n bottoms" "39" "70" "-1"
"862" "boy_tee_07.gif" "tops" "tops n bottoms" "38" "70" "-1"
"863" "boy_tee_08.gif" "tops" "tops n bottoms" "31" "70" "-1"
"864" "boy_body_04.gif" "body" "body" "26" "28" "-1"
"865" "glasses_01.gif" "hats" "hats" "35" "46" "-1"
"866" "girl_top_13.gif" "tops" "tops n bottoms" "40" "78" "-1"
"867" "girl_skirt_07.gif" "bottoms" "tops n bottoms" "38" "96" "-1"
"868" "girl_skirt_06.gif" "bottoms" "tops n bottoms" "37" "97" "-1"
"869" "girl_pants_12.gif" "pants" "underware" "40" "78" "-1"
"870" "girl_pants_11.gif" "pants" "underware" "39" "70" "-1"
"871" "girl_pants_10.gif" "pants" "underware" "32" "73" "-1"
"872" "girl_makeup_10.gif" "pants" "underware" "37" "47" "-1"
"873" "girl_hair_30.gif" "hair" "hair" "32" "6" "-1"
"874" "girl_hair_29.gif" "hair" "hair" "17" "23" "-1"
"875" "extensions_02.gif" "hair" "hair" "26" "19" "-1"
"876" "extensions_01.gif" "hair" "hair" "32" "17" "-1"
"877" "dog.gif" "extras" "infront" "3" "87" "-1"
"878" "cat_black.gif" "extras" "infront" "7" "108" "-1"
"879" "cat_brown.gif" "extras" "infront" "7" "108" "-1"
"880" "boy_trousers_08.gif" "bottoms" "tops n bottoms" "39" "97" "-1"
"881" "boy_shoes_07.gif" "shoes" "shoes" "37" "118" "-1"
"882" "boy_shades_06.gif" "hats" "hats" "36" "48" "-1"
"883" "boy_shades_05.gif" "hats" "hats" "36" "47" "-1"
"884" "boy_shades_04.gif" "hats" "hats" "36" "47" "-1"
"885" "boy_shades_03.gif" "hats" "hats" "36" "47" "-1"
"886" "boy_shades_02.gif" "hats" "hats" "34" "46" "-1"
"887" "boy_shades_01.gif" "hats" "hats" "34" "46" "-1"
"888" "boy_jumper_02.gif" "tops" "tops n bottoms" "26" "65" "-1"
"889" "boy_jumper_01.gif" "tops" "tops n bottoms" "26" "69" "-1"
"890" "boy_hair_20.gif" "hair" "hair" "32" "22" "-1"
"891" "boy_hair_19.gif" "hair" "hair" "32" "15" "-1"
"892" "boy_hair_18.gif" "hair" "hair" "34" "26" "-1"
"893" "boy_hair_17.gif" "hair" "hair" "34" "26" "-1"
"894" "alien.gif" "body" "body" "27" "28" "-1"
"895" "baby_01.gif" "extras" "infront" "17" "65" "-1"
"896" "baby_02.gif" "extras" "infront" "17" "65" "-1"
"897" "baby_03.gif" "extras" "infront" "17" "65" "-1"
"898" "cat_white.gif" "extras" "infront" "7" "108" "-1"
"899" "computer.gif" "extras" "infront" "2" "100" "-1" """

def getDataSet():
    set = []
    items = configdata.split('\n')
    for item in items:
        item = item.split(' ')
        set.append(map(lambda s:s.strip('"'), item))
    return set
    
    
def wget (fname):
    os.spawnlp(os.P_WAIT, '/sw/bin/wget', 'wget', fname)
    
path=r'http://www.stortroopers.com/goth/data/images/articles/'
elements = getDataSet()
for e in elements:
    print e[ImageName]
    wget(path + e[ImageName])

