#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
from modulesZ import *
from modulesA import *
"""-----------------------------"""

def CATEGORIES():
	'''------------------------------
	---MAIN--------------------------
	------------------------------'''
	CATEGORIES_SEARCH(mode=30, url="") #חיפוש
	addDir(addonString(30000).encode('utf-8'),'MyMusic',100,featherenceserviceicons_path + 'star.png',addonString_servicefeatherence(32800).encode('utf-8'),'1',0,getAddonFanart(100)) #My Music
	addDir(addonString(30001).encode('utf-8'),'',101,featherenceserviceicons_path + 'sod.png',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30001).encode('utf-8')),'1',0,getAddonFanart(101)) #Israeli Music
	addDir(addonString(30011).encode('utf-8'),'',111,featherenceserviceicons_path + 'us.png',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30011).encode('utf-8')),'1',0,getAddonFanart(111)) #Foreign Music
	'''---------------------------'''
	addDir(addonString(30022).encode('utf-8'),'',114,featherenceserviceicons_path + 'director.png',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30022).encode('utf-8')),'1',0,getAddonFanart(114)) #Fashion Shows
	'''---------------------------'''
	addDir(addonString(30018).encode('utf-8'),'',118,featherenceserviceicons_path + 'classical.png',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30018).encode('utf-8')),'1',0,getAddonFanart(118)) #Classical Music
	addDir(addonString(30019).encode('utf-8'),'',119,featherenceserviceicons_path + 'radio.png',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30019).encode('utf-8')),'1',0,getAddonFanart(119)) #Radio
	addDir(localize(10516),'ActivateWindow(10502,special://userdata/)',201,featherenceserviceicons_path + 'music.png',"Local Kodi's music library",'1',0,getAddonFanart(100)) #Local Library
	
def CATEGORIES100(name, iconimage, desc, fanart):
	'''------------------------------
	---My-Music----------------------
	------------------------------'''
	background = 100
	
	'''כפתור מוזיקה חדש..'''
	addDir(addonString_servicefeatherence(32450).encode('utf-8') % (addonString(300).encode('utf-8')),"New",20,featherenceserviceicons_path + 'clipboard.png',addonString_servicefeatherence(32451).encode('utf-8') + addonString_servicefeatherence(32452).encode('utf-8') + addonString_servicefeatherence(32453).encode('utf-8'),'s',0,getAddonFanart(background))
	
	'''רשימת השמעה 1'''
	if Custom_Playlist1_ID != "": addDir(Custom_Playlist1_Name,Custom_Playlist1_ID,18,Custom_Playlist1_Thumb,Custom_Playlist1_Description,'1',0,getAddonFanart("Custom_Playlist1")
	'''רשימת השמעה 2'''
	if Custom_Playlist2_ID != "": addDir(Custom_Playlist2_Name,Custom_Playlist2_ID,18,Custom_Playlist2_Thumb,Custom_Playlist2_Description,'2',0,getAddonFanart("Custom_Playlist2")
	'''רשימת השמעה 3'''
	if Custom_Playlist3_ID != "": addDir(Custom_Playlist3_Name,Custom_Playlist3_ID,18,Custom_Playlist3_Thumb,Custom_Playlist3_Description,'3',0,getAddonFanart("Custom_Playlist3")
	'''רשימת השמעה 4'''
	if Custom_Playlist4_ID != "": addDir(Custom_Playlist4_Name,Custom_Playlist4_ID,18,Custom_Playlist4_Thumb,Custom_Playlist4_Description,'4',0,getAddonFanart("Custom_Playlist4")
	'''רשימת השמעה 5'''
	if Custom_Playlist5_ID != "": addDir(Custom_Playlist5_Name,Custom_Playlist5_ID,18,Custom_Playlist5_Thumb,Custom_Playlist5_Description,'5',0,getAddonFanart("Custom_Playlist5")
	'''רשימת השמעה 6'''
	if Custom_Playlist6_ID != "": addDir(Custom_Playlist6_Name,Custom_Playlist6_ID,18,Custom_Playlist6_Thumb,Custom_Playlist6_Description,'6',0,getAddonFanart("Custom_Playlist6")
	'''רשימת השמעה 7'''
	if Custom_Playlist7_ID != "": addDir(Custom_Playlist7_Name,Custom_Playlist7_ID,18,Custom_Playlist7_Thumb,Custom_Playlist7_Description,'7',0,getAddonFanart("Custom_Playlist7")
	'''רשימת השמעה 8'''
	if Custom_Playlist8_ID != "": addDir(Custom_Playlist8_Name,Custom_Playlist8_ID,18,Custom_Playlist8_Thumb,Custom_Playlist8_Description,'8',0,getAddonFanart("Custom_Playlist8")
	'''רשימת השמעה 9'''
	if Custom_Playlist9_ID != "": addDir(Custom_Playlist9_Name,Custom_Playlist9_ID,18,Custom_Playlist9_Thumb,Custom_Playlist9_Description,'9',0,getAddonFanart("Custom_Playlist9")
	'''רשימת השמעה 10'''
	if Custom_Playlist10_ID != "": addDir(Custom_Playlist10_Name,Custom_Playlist10_ID,18,Custom_Playlist10_Thumb,Custom_Playlist10_Description,'10',0,getAddonFanart("Custom_Playlist10")
	
	if Custom_10001 == "true" and 1 + 1 == 3: addDir(addonString(30050).encode('utf-8'),'',10001,featherenceserviceicons_path + 'star.png',addonString(30051).encode('utf-8'),'1',0,'') #AMIR ELGAZAR PLAYLISTS
	if Custom_10002 == "true":
		'''Tomer Dror's Playlists'''
		thumb = os.path.join(addonPath,'icon.png')
		fanart = os.path.join(featherenceservice_path,'fanart.jpg')
		list = []
		list.append('&youtube_pl=PL9aMpOzf_PLV_Jex7GIRlGNGC7Y6nPpm8')
		addDir(addonString(30052).encode('utf-8'),list,17,thumb,'Thanks and credits to Tomer Dror.','1',0,fanart)
	
	if Custom_10003 == "true":
		'''Talia Kahalani's Playlists'''
		thumb = os.path.join(addonPath,'icon.png')
		fanart = os.path.join(featherenceservice_path,'fanart.jpg')
		list = []
		list.append('&youtube_pl=PLxMyxN4aYD2nPziqfqff8d_cu4xUnv0Ku')
		addDir(addonString(30053).encode('utf-8'),list,17,thumb,'Thanks and credits to Talia Kahalani.','1',0,fanart)
	
	if xbmc.getCondVisibility('Skin.HasSetting(Admin)'):
		list = []
		list.append('&youtube_ch=ShlomoArtziOfficial')
		addDir('test',list,17,"",'test','1',0,"")

def CATEGORIES10001(name, iconimage, desc, fanart):
	if name == None: name = ""
	else: name = name + newline
	
	
	'''Easy Listening, Love songs & Bellads'''
	thumb = 'http://orig15.deviantart.net/03ff/f/2010/027/5/c/best_music_logo_by_graphics4fun.png'
	fanart = 'http://ihdimages.com/wp-content/uploads/2014/11/dance_music_wallpaper_free_hd.jpg'
	addDir('Easy Listening, Love songs & Bellads',templates2_path + 'Easy Listening, Love songs & Bellads Personal Collection.txt',2,thumb,name + '','1',0,fanart)
	
	'''Elvis Presley Full Discografia Songs''' 
	thumb = 'http://the100.ru/images/lovers/id1473/elvis-aaron-presley-lovers-3626.jpg'
	fanart = 'http://2.bp.blogspot.com/_UQwx9AN7V_Q/TFm3agCcnCI/AAAAAAAAAgg/Pi8rzmey-uA/s1600/elvis-presley.jpg'
	addDir('Elvis Presley Full Discografia Songs',templates2_path + 'Elvis Presley Full Discografia Songs.txt',2,thumb,name + 'The first comprehensive collection in Kodi history','1',0,fanart) 
	
	'''Elton John Personal Collection'''
	thumb = 'https://upload.wikimedia.org/wikipedia/en/thumb/7/7d/GreatestHits19761986EltonJohn.jpg/220px-GreatestHits19761986EltonJohn.jpg'
	fanart = 'http://www.kwiknews.my/sites/default/files/styles/kwik_inner_cover/public/elton.john_.jpg?itok=eUB3cG36'
	addDir('Elton John Personal Collection',templates2_path + 'Elton John Personal Collection.txt',2,thumb,name + 'אלטון גון - אוסף אישי','1',0,fanart)
	
	'''billboard top 10 All The Time'''
	thumb = 'http://www.webgranth.com/wp-content/uploads/2013/07/Music-girl-WallPaper.jpg'
	fanart = 'https://str.your-pictionary.com/2015/01/30/image-gallary-5-beautiful-cool-wallpaper-designs-for-girls-b-o-ibackgroundz.com.jpg'
	addDir('billboard top 10 All The Time',templates2_path + 'billboard top 10 All The Time.txt',2,thumb,name + '','1',0,fanart)
	
	'''My Very First Playlist Ever'''
	thumb = 'http://orig15.deviantart.net/03ff/f/2010/027/5/c/best_music_logo_by_graphics4fun.png'
	fanart = 'http://allwallpapersnew.com/wp-content/gallery/i-love-music-wallpapers/__i_love_music___wallpaper_by_nnamefx-d48f0im.jpg'
	addDir('My Very First Playlist Ever',templates2_path + 'My Very First Playlist Ever.txt',2,thumb,name + 'my Personal Collection','1',0,fanart)
	
	'''Elvis Presley Mixes Song''' 
	thumb = 'http://the100.ru/images/lovers/id1473/elvis-aaron-presley-lovers-3626.jpg'
	fanart = 'http://2.bp.blogspot.com/_UQwx9AN7V_Q/TFm3agCcnCI/AAAAAAAAAgg/Pi8rzmey-uA/s1600/elvis-presley.jpg'
	addDir('Elvis Presley Mixes Song',templates2_path + 'Elvis Presley Mixes Song.txt',2,thumb,name + 'Elvis never left the building, turn on speakers and start to get excited','1',0,fanart) 
	
	'''George Michael & wham'''
	thumb = 'http://i234.photobucket.com/albums/ee136/suwarnaadi/hair/GeorgeMichaelshortsideshair.jpg'
	fanart = 'http://www.golden80s.com/wp-content/uploads/2014/05/Wham-head.jpg'
	addDir('George Michael & wham',templates2_path + 'George Michael & wham.txt',2,thumb,name + 'Personal Collection','1',0,fanart)
	
	'''bob dylan'''
	thumb = 'https://s3.amazonaws.com/rapgenius/600full-the-best-of-bob-dylan-cover.jpg'
	fanart = 'http://zetaestaticos.com/cordoba/img/noticias/0/950/950919_1.jpg'
	addDir('Top Songs Of Bob Dylan',templates2_path + 'Top Songs Of Bob Dylan.txt',2,thumb,desc + '','1',0,fanart)
	
	'''Great French Collection'''
	thumb = 'http://images.travelpod.com/tripwow/photos/ta-00b7-d4d4-11a6/arc-de-triomphe-paris-france+1152_12905284514-tpfil02aw-11867.jpg'
	fanart = 'http://www.wallpapersbyte.com/wp-content/uploads/2015/06/Downolad-HD-Wallpaper-France-Paris-City-Eiffel-Tower-Sunset-WallpapersByte-com-1920x1080.jpg'
	addDir('Great French Collection',templates2_path + 'Great French Collection.txt',2,thumb,name + '','1',0,fanart)
	
	'''Rain songs in a playlist'''
	thumb = 'http://laughingsquid.com/wp-content/uploads/Rain.jpg'
	fanart = 'http://www.artifacting.com/blog/wp-content/uploads/2012/10/Rain-Room.jpg'
	addDir('Rain songs in a playlist',templates2_path + 'Rain songs in a playlist.txt',2,thumb,name + '','1',0,fanart) 
	
	'''Jast Like A Woman'''
	thumb = 'http://www.libernia-magica.es/s/cc_images/cache_2458790013.jpg?t=1438345648'
	fanart = 'http://cdn.paper4pc.com/images/beautiful-blonde-wallpaper-25.jpg'
	addDir('Just Like A Woman',templates2_path + 'Just Like A Woman.txt',2,thumb,name + '','1',0,fanart)
	
	'''Greek party music''' 
	thumb = 'http://www.bestarabicmusic.net/wp-content/uploads/2012/07/arab-oud-300x220.jpg'
	fanart = 'https://aranui.com/wp-content/uploads/2014/11/borabora.jpg'
	addDir('Greek party music',templates2_path + 'Greek party music.txt',2,thumb,name + 'העריכה והבקשה של חברינו לקבוצה Yehuda Belhasin','1',0,fanart) 
	
	'''Greek Quiet music''' 
	thumb = 'http://www.bestarabicmusic.net/wp-content/uploads/2012/07/arab-oud-300x220.jpg'
	fanart = 'https://aranui.com/wp-content/uploads/2014/11/borabora.jpg'
	addDir('Greek Quiet music',templates2_path + 'Greek Quiet music.txt',2,thumb,name + 'העריכה והבקשה של חברינו לקבוצה Yehuda Belhasin','1',0,fanart) 
	
	'''love songs vol 1'''
	thumb = 'http://fullhdpictures.com/wp-content/uploads/2015/04/Beauty-Love-Wallpapers.jpg'
	fanart = 'http://www.hd-wallpapersdownload.com/upload/bulk-upload/hd-wallpaper-romantic-love.jpg'
	addDir('love songs vol 1',templates2_path + 'love songs vol 1.txt',2,thumb,name + 'love songs vol 1 - Personal Collection','1',0,fanart)
	
	'''My Generation'''
	thumb = 'http://cdn.scahw.com.au/cdn-1d0999afe8fe1c0/ImageVaultFiles/id_349131/cf_7/localworks_MyGeneration-628x387.JPG'
	fanart = 'https://i.ytimg.com/vi/d88YGB4hZow/maxresdefault.jpg'
	addDir('My Generation',templates2_path + 'My Generation.txt',2,thumb,name + '','1',0,fanart)
	
	'''Leonard Cohen'''
	thumb = 'http://i.telegraph.co.uk/multimedia/archive/02120/leonardcohen_2120582b.jpg'
	fanart = 'http://www.newyorker.com/wp-content/uploads/2015/02/Avishai-Cohen-Montreal-1189.jpg'
	addDir('Leonard Cohen',templates2_path + 'Leonard Cohen.txt',2,thumb,desc + '','1',0,fanart)
	
	'''The Beatles'''
	thumb = 'http://img2-ak.lst.fm/i/u/ar0/6a122bb0665d4d8ca0cc4c31e245ff55'
	fanart = 'http://p1.pichost.me/i/70/1943195.jpg'
	addDir('The Beatles',templates2_path + 'The Beatles.txt',2,thumb,name + '','1',0,fanart)

	'''אריק סיני'''
	thumb = 'http://stereo-ve-mono.com/sleeves/42/4265501a.jpg'
	fanart = 'https://i.ytimg.com/vi/eh6bNCq8vjE/maxresdefault.jpg'
	addDir('אריק סיני אוסף',templates2_path + 'Aric Sinai.txt',2,thumb,name + '','1',0,fanart)
	 
	'''אוסף ישראלי'''
	thumb = 'http://www.artishuk.co.il/UserFiles/Store/Products/Products/230x634453006475603750_M.png'
	fanart = 'http://www.pupic.co.il/UploadedImages/Original/%D7%9E%D7%95%D7%96%D7%99%D7%A7%D7%94%20%D7%99%D7%A9%D7%A8%D7%90%D7%9C%D7%99%D7%AA.jpg'
	addDir('ישראלי אוסף אישי',templates2_path + 'Israeli Collection.txt',2,thumb,name,'1',0,fanart)
	
	'''הגשש החיוור השירים'''
	thumb = 'https://atmag-static-timeout.netdna-ssl.com/misc/prev_images/images/%D7%AA%D7%A8%D7%91%D7%95%D7%AA/gashash.jpg'
	fanart = 'https://market.marmelada.co.il/photos/787481.jpg'
	addDir('הגשש החיוור שירים',templates2_path + 'Hagasach hahever songs.txt',2,thumb,name + '','1',0,fanart)
	
	'''ארבע אחר הצהריים'''
	thumb = 'http://th-pro.co.il/SiteImages/SiteImage_c98e320c-2103-4fb8-9c91-b2e8e4aa416a.jpg'
	fanart = 'http://www.women-zone.com/wp-content/uploads/2015/08/israel.jpg' 
	addDir('ארבע אחר הצהריים',templates2_path + 'Four in the afternoon.txt',2,thumb,name + 'מוקדש ל Oren Hagay חברינו לקבוצה Kodisrael.net','1',0,fanart)
	
	'''עוד מעט נהפוך לשיר הפרוייקט'''
	thumb = 'http://img2.timg.co.il/forums/1_116211607.jpg'
	fanart = 'http://www.ayaskitchen.com/forum/uploads/4187.jpg'
	addDir('עוד מעט נהפוך לשיר',templates2_path + 'Od Meat Nhafch Leshir.txt',2,thumb,name + 'ליום הזיכרון','1',0,fanart)

	'''שירי הלהקות הצבאיות'''
	thumb = 'http://blog.tapuz.co.il/charchanut/images/%7B8A174BD1-2035-45AF-B1D8-21ACA3646553%7D.jpg'
	fanart = 'https://i.ytimg.com/vi/t0couQwmgbc/maxresdefault.jpg'
	addDir('שירי הלהקות הצבאיות',templates2_path + 'The Israeli Army Song Collection.txt',2,thumb,name + 'ליום העצמאות','1',0,fanart)
	
	'''שלמה ארצי אוסף אישי'''
	thumb = 'http://www.nrg.co.il/images/archive/465x349/1/077/947.jpg'
	fanart = 'http://www.megapixel.co.il/mega/wp-content/uploads/2012/02/Shlomo-Artzi_so.jpg'
	addDir('שלמה ארצי אוסף אישי',templates2_path + 'Shlomo Artzi Personal Collection.txt',2,thumb,name + '','1',0,fanart)
	 
	'''אריק איינשטיין אוסף אישי'''
	thumb = 'http://www.maariv.co.il/download/pictures/%D7%90%D7%A8%D7%99%D7%A7%20%D7%90%D7%99%D7%99%D7%A0%D7%A9%D7%98%D7%99%D7%9F%203%20-%20%D7%A6%D7%99%D7%9C%D7%95%D7%9D%20%D7%9E%D7%A9%D7%94%20%D7%A9%D7%99%20%D7%A4%D7%9C%D7%90%D7%A9%2090%20480_2.jpg'
	fanart = 'http://www.haaretz.co.il/polopoly_fs/1.2490157.1416401072!/image/2643586370.jpg_gen/derivatives/size_936xAuto/2643586370.jpg'
	addDir('אריק איינשטיין אוסף אישי',templates2_path + 'Arik Einstein.txt',2,thumb,name + '','1',0,fanart)

	'''שירי יום השואה'''
	thumb = 'http://www.rimonschool.co.il/wp-content/uploads/2015/04/yezkor-11.jpg'
	fanart = 'http://blog.tapuz.co.il/momins/images/%7BF6AB614D-CC3F-45C2-97A8-9FB8C494FF16%7D.jpg'
	addDir('יום השואה שירים וסיפורים',templates2_path + 'Holocaust Day songs.txt',2,thumb,name + 'לזכר 6 מיליון יהודים','1',0,fanart)
	
	'''יהורם גאון'''
	thumb = 'http://www.srugim.co.il/wp-content/uploads/2016/06/50998baf638754820da8b0d28d313a4a.jpg'
	fanart = 'https://market.marmelada.co.il/photos/787402.jpg'
	addDir('יהורם גאון האוסף המחומש',templates2_path + 'YEHORAM  GAON.txt',2,thumb,name,'1',0,fanart)
	
	'''פלייליסט מזרחי שקט ורגוע''' 
	thumb = 'http://www.vehiclehi.com/thumbnails/detail/20121101/headphones%20women%20music%20headphones%20girl%201920x1080%20wallpaper_www.vehiclehi.com_28.jpg'
	fanart = 'http://i.ytimg.com/vi/vaQiwOi8Afk/maxresdefault.jpg'
	addDir('פלייליסט מזרחי שקט ורגוע',templates2_path + 'mizrahi Quiet playlist.txt',2,thumb,name + 'על פי בקשה של חברי הקבוצה (KODISRAEL.NET)','1',0,fanart) 
	
	'''פלייליסט מזרחי קיצבי דאנס'''
	thumb = 'http://www.commentsyard.com/cy/01/9086_original.gif'
	fanart = 'http://3.bp.blogspot.com/-_90x10bD8Xs/VIn8kUH4rwI/AAAAAAAAABo/Yif1L9eLyuE/s1600/music.jpg'
	addDir('פלייליסט מזרחי קיצבי דאנס',templates2_path + 'mizrahi party playlist.txt',2,thumb,name + 'על פי בקשה של חברי הקבוצה (KODISRAEL.NET)','1',0,fanart) 
	
	'''שירי יום הזיכרון לחללי מערכות ישראל ולנפגעי פעולות האיבה'''
	thumb = 'http://www.go4it.org.il/f/attachment.php?attachmentid=1787&stc=1&thumb=1&d=1240841639'
	fanart = 'https://i.ytimg.com/vi/79UUYR1gd2k/maxresdefault.jpg'
	addDir('שירי יום הזיכרון לחללי מערכות ישראל ולנפגעי פעולות האיבה',templates2_path + 'IDF memorial day.txt',2,thumb,name + 'מוקדש לכל מי שהקריב את נפשו למען הגנת המדינה','1',0,fanart)

def CATEGORIES10002(name, iconimage, desc, fanart):
	if name == None: name = ""
	else: name = name + newline
	
def CATEGORIES101(name, iconimage, desc, fanart):
	'''Israeli Music'''
	addDir(addonString(30001).encode('utf-8'),'',10101,featherenceserviceicons_path + "music.png",addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30001).encode('utf-8')),'1',0, getAddonFanart(10101, default="") #Israeli Music
	addDir(addonString(30005).encode('utf-8'),'',10105,featherenceserviceicons_path + "radio.png",addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30005).encode('utf-8')),'1',0, getAddonFanart(10105, default="http://telavivparty.com/wp-content/uploads/2016/08/Light-House-Club-Tel-Aviv.jpg") #Israeli Djs
	
	addDir(addonString(30006).encode('utf-8'),'',10106,featherenceserviceicons_path + "music.png",addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30006).encode('utf-8')),'1',0, getAddonFanart(10106, default="http://haflla.com/wp-content/uploads/2014/10/pic4.jpg") #Mizrahit Music
	
def CATEGORIES111(name, iconimage, desc, fanart):
	'''Foreign Music'''
	addDir(addonString(30011).encode('utf-8'),'',11101,featherenceserviceicons_path + "music.png",addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30011).encode('utf-8')),'1',0, getAddonFanart(11101)) #Foreign Music
	addDir(addonString(30015).encode('utf-8'),'',11105,featherenceserviceicons_path + "radio.png",addonString(30015).encode('utf-8'),'1',0, getAddonFanart(11105, default="https://tiestoclublife.files.wordpress.com/2014/05/dj_tiesto_club_life_2014_img372.jpg") #Foreign Djs

def CATEGORIES10101(name, iconimage, desc, fanart):
	'''------------------------------
	---Israeli-Music-----------------
	------------------------------'''
	background = 101
	commonsearch = 'commonsearch101'
	
	CATEGORIES_RANDOM(background,fanart)
	
	CATEGORIES10101Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה

	'''אביתר בנאי'''
	list = [] ; se = '"addonString(30101)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30101)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30101)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30101).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://images.mouse.co.il/storage/7/f/eviatar-ggg.jpg',addonString(30201).encode('utf-8'),'1',0,fanart)
		
	'''אברהם טל'''
	list = [] ; se = '"addonString(30102)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30102)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30102)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30102).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://images.mouse.co.il/storage/a/d/Avraham_Tal_490.jpg',addonString(30202).encode('utf-8'),'1',0,fanart)

	'''אתניקס'''
	list = [] ; se = '"addonString(30105)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30105)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30105)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	
	addDir(addonString(30105).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://img.mako.co.il/2013/05/21/etnix_prn_c.jpg',addonString(30205).encode('utf-8'),'1',0,fanart)
	
	'''פורטיסחרוף'''
	list = [] ; se = '"addonString(30106)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30106)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30106)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30106).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.yosmusic.com/images/articles/big/fortis1284-b.jpg',addonString(30206).encode('utf-8'),'1',0,fanart)
		
	'''גיא ויהל'''
	list = [] ; se = '"addonString(30108)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30108)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30108)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30108).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://i.ytimg.com/vi/9fkcGdgj-iI/hqdefault.jpg',addonString(30208).encode('utf-8'),'1',0,fanart)
	
	'''דני סנדרסון'''
	list = [] ; se = '"addonString(30111)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30111)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30111)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30111).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://images1.calcalist.co.il/PicServer2/20122005/158200/YE0415562_l.jpg',addonString(30211).encode('utf-8'),'1',0,fanart)
	
	'''הראל סקעת'''
	list = [] ; se = '"addonString(30113)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30113)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30113)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30113).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'https://i.ytimg.com/i/BbOw6LiHmj6L9o_HlMvKKg/mq1.jpg?v=51c9be2d',addonString(30213).encode('utf-8'),'1',0,fanart)
	
	'''הדודאים''' 
	list = [] ; se = '"addonString(30148)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30148)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30148)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30148).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'https://i.ytimg.com/vi/vxA1AlH9o-0/hqdefault.jpg',addonString(30248).encode('utf-8'),'1',0,fanart) 

	'''כוורת גזוז דודה'''
	list = [] ; se = '"addonString(30115)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30115)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30115)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30115).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://3.bp.blogspot.com/-MQNn8bDIkIU/TcN-z5QEkkI/AAAAAAAABCM/xYuRV3ht--I/s1600/%25D7%2593%25D7%2595%25D7%2593%25D7%2594+%25D7%25A6%25D7%2599%25D7%259C%25D7%2595%25D7%259D+%25D7%2590%25D7%2591%25D7%2599+%25D7%2592%25D7%25A0%25D7%2595%25D7%25A8.jpg',addonString(30215).encode('utf-8'),'1',0,fanart)
	
	'''מוש בן ארי ולהקת שבע'''
	list = [] ; se = '"addonString(30121)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30121)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30121)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30121).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.nrg.co.il/images/archive/408x322/692/069.jpg',addonString(30221).encode('utf-8'),'1',0,fanart)

	'''מזי כהן'''
	list = [] ; se = '"addonString(30120)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30120)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30120)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30120).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'https://i.ytimg.com/vi/3JAAD8Ptq00/maxresdefault.jpg',addonString(30220).encode('utf-8'),'1',0,fanart)
	
	'''מירי מסיקה'''
	list = [] ; se = '"addonString(30123)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30123)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30123)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30123).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'https://i.ytimg.com/i/7cwmZGtlWPDkkEWsxkZd-Q/mq1.jpg?v=54998b82',addonString(30223).encode('utf-8'),'1',0,fanart)
	
	'''משינה'''
	list = [] ; se = '"addonString(30126)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30126)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30126)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30126).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://msc.wcdn.co.il/w/w-700/253820-5.jpg',addonString(30226).encode('utf-8'),'1',0,fanart)
	
	'''נתן גושן'''
	list = [] ; se = '"addonString(30127)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30127)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30127)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30127).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'https://upload.wikimedia.org/wikipedia/he/2/27/%D7%A0%D7%AA%D7%9F_%D7%92%D7%95%D7%A9%D7%9F.jpg',addonString(30227).encode('utf-8'),'1',0,fanart)
	
	'''סטטיק ובן אל'''
	list = [] ; se = '"addonString(30134)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30134)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30134)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30134).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://media.shironet.mako.co.il/media/performers/heb/0/764/profile/764_t275.jpg?rnd=58',addonString(30234).encode('utf-8'),'1',0,fanart)
	
	'''עברי לידר'''
	list = [] ; se = '"addonString(30130)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30130)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30130)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30130).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://media.shironet.mako.co.il/media/performers/heb/0/764/profile/764_t275.jpg?rnd=58',addonString(30230).encode('utf-8'),'1',0,fanart)
	
	'''עידן רייכל'''
	list = [] ; se = '"addonString(30132)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30132)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30132)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30132).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'https://yt3.ggpht.com/-vsBWN1RBQuk/AAAAAAAAAAI/AAAAAAAAAAA/SWZEbbG5oUY/s100-c-k-no/photo.jpg',addonString(30232).encode('utf-8'),'1',0,fanart)
  
	'''קרן פלס'''
	list = [] ; se = '"addonString(30138)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30138)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30138)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30138).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/KerenPelesNew.jpg/375px-KerenPelesNew.jpg',addonString(30238).encode('utf-8'),'1',0,fanart)
	
	'''ריטה'''
	list = [] ; se = '"addonString(30139)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30139)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30139)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30139).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://img.mako.co.il/2013/02/07/rita_promo_bww_c.jpg',addonString(30239).encode('utf-8'),'1',0,fanart)
	
	'''רמי קליינשטיין'''
	list = [] ; se = '"addonString(30140)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30140)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30140)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30140).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://images1.ynet.co.il/PicServer2/28102008/1770103/2_wh.jpg',addonString(30240).encode('utf-8'),'1',0,fanart)
	
	'''שירי מימון'''
	list = [] ; se = '"addonString(30141)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30141)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30141)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30141).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Sm_album3.jpg/250px-Sm_album3.jpg',addonString(30241).encode('utf-8'),'1',0,fanart)
	
	'''שלום חנוך'''
	list = [] ; se = '"addonString(30142)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30142)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30142)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30142).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'https://yt3.ggpht.com/-6DiGw2l8Nrk/AAAAAAAAAAI/AAAAAAAAAAA/3qnrk75SjaA/s100-c-k-no/photo.jpg',addonString(30242).encode('utf-8'),'1',0,fanart)

	'''שלמה ארצי'''
	list = [] ; se = '"addonString(30144)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30144)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30144)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30144).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.nrg.co.il/images/archive/465x349/1/403/734.jpg',addonString(30244).encode('utf-8'),'1',0,"http://blinker.co.il/wp-content/uploads/2012/08/shlomo-artzi-1-e1345892186997.jpg")
	
	'''שלישית גשר הירקון''' 
	list = [] ; se = '"addonString(30149)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30149)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30149)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30149).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'https://www.kedem-auctions.com/sites/default/files/sale/1300/19724.jpg',addonString(30249).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES10101A(name, iconimage, desc, fanart) #דף הבא
		
def CATEGORIES10105(name, iconimage, desc, fanart):
	'''------------------------------
	---Israeli-Djs-------------------
	------------------------------'''
	background = 105
	
	CATEGORIES_RANDOM(background,fanart)
	CATEGORIES10105Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
	'''Astrix'''
	list = []
	se = '"addonString(30614)' + space + 'DJ"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list.append('&youtube_ch=ASTRIXtv')
	addDir(addonString(30614).encode('utf-8'),list,17,'https://static.djguide.nl/image/djfotos/astrix.jpg',addonString(30615).encode('utf-8'),'1',0,"http://mixing.dj/wp-content/uploads/2016/02/astrix.jpg")
	
	'''Dor Dekel'''
	list = []
	se = '"addonString(30602)' + space + 'DJ"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list.append('&youtube_pl=PL836BAF6EB6F903BF')
	list.append('&youtube_pl=PL525196B53E11F4E7')
	addDir(addonString(30602).encode('utf-8'),list,17,'https://pbs.twimg.com/profile_images/3391613680/c69b693265bf51f1293c71ef3ef9bf77.jpeg',addonString(30603).encode('utf-8'),'1',0,"https://pbs.twimg.com/profile_images/3391613680/c69b693265bf51f1293c71ef3ef9bf77.jpeg")
	
	'''Elon Matana'''
	list = []
	se = '"addonString(30612)' + space + 'DJ"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list.append('&youtube_ch=ElonMatanaOfficial')
	addDir(addonString(30612).encode('utf-8'),list,17,'https://yt3.ggpht.com/-go0RRo59atU/AAAAAAAAAAI/AAAAAAAAAAA/lkZwlOgFbnI/s100-c-k-no-mo-rj-c0xffffff/photo.jpg',addonString(30613).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/8BDh-wDN1vA/maxresdefault.jpg")
	
	'''Itay Galo'''
	list = []
	se = '"addonString(30610)' + space + 'DJ"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list.append('&youtube_id=8B32a1T8YAs')
	list.append('&youtube_id=4x9SnLNoDow')
	addDir(addonString(30610).encode('utf-8'),list,17,'https://i1.sndcdn.com/avatars-000068050274-lxbtnx-t500x500.jpg',addonString(30611).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/WHzyA-POMzQ/maxresdefault.jpg")
	
	'''Leibo'''
	list = []
	se = '"addonString(30600)' + space + 'DJ"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list.append('&youtube_ch=LEIBOTV')
	addDir(addonString(30600).encode('utf-8'),list,17,'https://yt3.ggpht.com/-6soiuKo5St8/AAAAAAAAAAI/AAAAAAAAAAA/G1GBvGCLKeI/s100-c-k-no-mo-rj-c0xffffff/photo.jpg',addonString(30601).encode('utf-8'),'1',0,"http://eco99fm.maariv.co.il/download/Sets/pictures/dj_set_leibo_02.jpg")
	
	'''Offer Nissim'''
	list = []
	se = '"addonString(30608)' + space + 'DJ"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list.append('&youtube_ch=OfferNissimOfficial')
	addDir(addonString(30608).encode('utf-8'),list,17,'http://bemynextsong.com/images/artists/174/thmb/20090327110019_offer_nissim-2-5cd1b-800.jpg',addonString(30609).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/vkQuE86rvng/maxresdefault.jpg")
	
	'''Omri Guetta'''
	list = []
	se = '"addonString(30604)' + space + 'DJ"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	addDir(addonString(30604).encode('utf-8'),list,17,'http://scontent.cdninstagram.com/t51.2885-15/s750x750/sh0.08/e35/13707368_868781096559186_1918315964_n.jpg',addonString(30605).encode('utf-8'),'1',0,"http://scontent.cdninstagram.com/t51.2885-15/s750x750/sh0.08/e35/13707368_868781096559186_1918315964_n.jpg")
	
	'''Skazi'''
	list = []
	se = '"addonString(30606)' + space + 'DJ"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list.append('&youtube_ch=DJSkaziOfficial')
	addDir(addonString(30606).encode('utf-8'),list,17,'http://www.radioandmusic.com/sites/www.radioandmusic.com/files/images/entertainment/2015/11/28/Skazi.jpg',addonString(30607).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/c7RmAuD88-w/maxresdefault.jpg")
	
	'''Guy Gerber'''
	list = []
	se = '"addonString(30618)' + space + 'DJ"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	addDir(addonString(30618).encode('utf-8'),list,17,'https://en.wikipedia.org/wiki/File:Guy-gerber5.jpg',addonString(30619).encode('utf-8'),'1',0,"https://upload.wikimedia.org/wikipedia/en/9/9f/Guy-gerber5.jpg")
	
	'''Yahel'''
	list = []
	se = '"addonString(30616)' + space + 'DJ"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list.append('&youtube_ch=shermanyahel')
	addDir(addonString(30616).encode('utf-8'),list,17,'https://static.djguide.nl/image/djfotos/astrix.jpg',addonString(30617).encode('utf-8'),'1',0,"http://mixing.dj/wp-content/uploads/2016/02/astrix.jpg")
	
	
	CATEGORIES10105A(name, iconimage, desc, fanart) #דף הבא
	
def CATEGORIES10106(name, iconimage, desc, fanart):
	'''------------------------------
	---Mizrahit-Music----------------
	------------------------------'''
	background = 106
	
	CATEGORIES_RANDOM(background,fanart)
	'''חיפוש'''
	addDir(localize(137),'שיר',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(32416).encode('utf-8') % (addonString(30021).encode('utf-8')),'1',0,fanart)
	
	CATEGORIES10106Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה

	'''אייל גולן'''
	thumb = 'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg'
	fanart = 'http://eco99fm.maariv.co.il/download/pictures/Show_245_4506.jpg'
	list = [] ; se = '"addonString(30103)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30103)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30103)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30103).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,thumb,addonString(30203).encode('utf-8'),'1',0,fanart)
	
	'''דודו אהרון'''
	thumb = ''
	fanart = ''
	list = [] ; se = '"addonString(30103)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30103)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30103)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30103).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(30203).encode('utf-8'),'1',0,fanart)
	addDir(addonString(30107).encode('utf-8'),list,17,'http://www.klr-lior.com/wp-content/gallery/omanim/dudu_aharon-hero_c.jpg',addonString(30207).encode('utf-8'),'1',0,fanart)
	
	'''הפרויקט של רביבו'''
	thumb = ''
	fanart = ''
	list = [] ; se = '"addonString(30103)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30103)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30103)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30103).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(30203).encode('utf-8'),'1',0,fanart)
	addDir(addonString(30112).encode('utf-8'),list,17,'http://img.mako.co.il/2012/08/23/revivo_project_purple_c.jpg',addonString(30212).encode('utf-8'),'1',0,fanart)
	
	'''זוהר ארגוב'''
	thumb = ''
	fanart = ''
	list = [] ; se = '"addonString(30103)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30103)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30103)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30103).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(30203).encode('utf-8'),'1',0,fanart)
	addDir(addonString(30128).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/he/thumb/6/67/Argov.jpg/200px-Argov.jpg',addonString(30228).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/nM8XuZZQnt4/maxresdefault.jpg")
	
	'''חיים משה'''
	thumb = ''
	fanart = ''
	list = [] ; se = '"addonString(30103)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30103)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30103)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30103).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(30203).encode('utf-8'),'1',0,fanart)
	addDir(addonString(30114).encode('utf-8'),list,17,'http://images.one.co.il/images/mag/450_250/gg789176.jpg',addonString(30214).encode('utf-8'),'1',0,fanart)
	
	'''יעקב חתן'''
	thumb = ''
	fanart = ''
	list = [] ; se = '"addonString(30103)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30103)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30103)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30103).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(30203).encode('utf-8'),'1',0,fanart)
	addDir(addonString(30116).encode('utf-8'),list,17,'https://yt3.ggpht.com/-_rt6N50COLw/AAAAAAAAAAI/AAAAAAAAAAA/F_g5RBGIXfo/s100-c-k-no/photo.jpg',addonString(30216).encode('utf-8'),'1',0,fanart)
	
	'''ישי לוי'''
	thumb = 'http://harif.co.il/wp-content/uploads/2010/07/%D7%99%D7%A9%D7%99-%D7%9C%D7%95%D7%99-%D7%9E%D7%A8%D7%92%D7%A9-%D7%91%D7%A6%D7%99%D7%9C%D7%95%D7%9E%D7%99-%D7%94%D7%A7%D7%9C%D7%99%D7%A4-%D7%AA%D7%95%D7%93%D7%94.jpg'
	fanart = ''
	list = [] ; se = '"addonString(30103)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30103)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30103)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30117).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(30217).encode('utf-8'),'1',0,fanart)

	'''ליאור נרקיס'''
	thumb = 'http://bsn.co.il/sites/default/files/styles/home_page_main_story_image_480x269/public/%D7%9C%D7%99%D7%90%D7%95%D7%A8%20%D7%A0%D7%A8%D7%A7%D7%99%D7%A1.jpg'
	fanart = ''
	list = [] ; se = '"addonString(30103)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30103)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30103)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30118).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(30218).encode('utf-8'),'1',0,fanart)
	 	
	'''מושיק עפיה'''
	thumb = 'https://yt3.ggpht.com/-4IayEL0C0Rs/AAAAAAAAAAI/AAAAAAAAAAA/kEV66on9DOM/s100-c-k-no/photo.jpg'
	fanart = ''
	list = [] ; se = '"addonString(30103)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30103)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30103)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30122).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,fanart,addonString(30222).encode('utf-8'),'1',0,fanart)
	 
	'''מאור אדרי'''
	thumb = 'http://img.mako.co.il/2012/09/12/maor_edri_suit_c.jpg'
	fanart = ''
	list = [] ; se = '"addonString(30103)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30103)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30103)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30124).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(30224).encode('utf-8'),'1',0,fanart)
	
	'''משה פרץ'''
	thumb = 'https://i.ytimg.com/i/0ebT4a-IyuY61X8py3nzsg/mq1.jpg?v=52124db3'
	fanart = ''
	list = [] ; se = '"addonString(30103)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30103)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30103)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30125).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(30225).encode('utf-8'),'1',0,fanart)
	
	'''עדן בן זקן'''
	thumb = ''
	fanart = ''
	list = [] ; se = '"addonString(30103)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30103)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30103)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30103).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(30203).encode('utf-8'),'1',0,fanart)
	addDir(addonString(30146).encode('utf-8'),list,17,'http://img.mako.co.il/2015/05/28/EDENBENZAKEN_c.jpg',addonString(30246).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/nwpLIXdrHS0/maxresdefault.jpg")
	
	'''מושיק עפיה'''
	thumb = ''
	fanart = ''
	list = [] ; se = '"addonString(30103)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30103)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30103)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30103).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(30203).encode('utf-8'),'1',0,fanart)
	addDir(addonString(30122).encode('utf-8'),list,17,'https://yt3.ggpht.com/-4IayEL0C0Rs/AAAAAAAAAAI/AAAAAAAAAAA/kEV66on9DOM/s100-c-k-no/photo.jpg',addonString(30222).encode('utf-8'),'1',0,fanart)

	'''עומר אדם'''
	thumb = 'http://www.forbes.co.il/download/pictures/%D7%A2%D7%95%D7%9E%D7%A8%20%D7%90%D7%93%D7%9D%20490.jpg'
	fanart = 'https://i.ytimg.com/vi/t-kLLFVMCgo/maxresdefault.jpg'
	list = [] ; se = '"addonString(30133)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30133)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30133)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30133).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(30233).encode('utf-8'),'1',0,fanart)
	
	'''פאר טסי'''
	thumb = 'https://yt3.ggpht.com/-XdArdL_W374/AAAAAAAAAAI/AAAAAAAAAAA/phGLZNk8iwU/s100-c-k-no/photo.jpg'
	fanart = ''
	list = [] ; se = '"addonString(30135)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30135)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30135)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30135).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,thumb,addonString(30235).encode('utf-8'),'1',0,fanart)
	
	'''קובי פרץ'''
	thumb = 'https://i.ytimg.com/i/GYqX6zfso91VDawbH_Nukw/mq1.jpg?v=4f5f486f'
	list = [] ; se = '"addonString(30103)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30103)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30103)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30137).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,thumb,addonString(30237).encode('utf-8'),'1',0,fanart)

	'''שרית חדד'''
	thumb = 'https://i.ytimg.com/i/0m-czKbg-tL7J61RDdU1rg/mq1.jpg?v=54ac3da1'
	fanart = 'https://upload.wikimedia.org/wikipedia/he/e/e8/%D7%A9%D7%A8%D7%99%D7%AA_%D7%97%D7%93%D7%93_%D7%A9%D7%A8%D7%94_%D7%A9%D7%A8%D7%94.jpeg'
	list = [] ; se = '"addonString(30145)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30145)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30145)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30145).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,thumb,addonString(30245).encode('utf-8'),'1',0,fanart)
	
	'''שני יצהרי'''
	thumb = 'http://images.one.co.il/images/mag/450_250/gg789176.jpg'
	fanart = 'https://i.ytimg.com/vi/5WFr624zttI/maxresdefault.jpg'
	list = [] ; se = '"addonString(30147)' + space + 'addonString(30027)"' ; list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list2 = [] ; se = '"addonString(30147)' + space + 'addonString(30028)"' ; list2.append('&youtube_se=' + se + '&videoDefinition=high&')
	list3 = [] ; se = '"addonString(30147)' + space + 'addonString(30026)"' ; list3.append('&youtube_se=' + se + '&videoDuration=long&&videoDefinition=high&')
	addDir(addonString(30147).encode('utf-8'),{ 'Karaoke': list2, 'Liveshows': list3, 'Songs': list },17,thumb,addonString(30247).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES10106A(name, iconimage, desc, fanart) #דף הבא
	
def CATEGORIES11101(name, iconimage, desc, fanart):
	'''------------------------------
	---Foreign-Music-----------------
	------------------------------'''
	background = 111
	commonsearch = 'commonsearch111'
	
	CATEGORIES_RANDOM(background,fanart)
	'''חיפוש'''
	addDir(localize(137),'song',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(32416).encode('utf-8') % (addonString(30021).encode('utf-8')),'1',0,fanart)
	
	CATEGORIES11101Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
	'''Adele'''
	list = []
	list.append('&youtube_pl=PL2jZGLrfnPrwKpGWByChK2ujJsh8XGT1u')
	list.append('&youtube_pl=PL9319650950E41B78')
	list.append('&youtube_pl=PL1C76D5F2FB130533')             
	list.append('&youtube_pl=PLEEyQEShYtdXMVAiHjpbSAIXRmuaxkiac') 
	addDir(addonString(30327).encode('utf-8'),list,17,'http://cdn.cultofmac.com/wp-content/uploads/2015/11/adele-third-album-25.jpg',addonString(30427).encode('utf-8'),'1',0,"http://yesofcorsa.com/wp-content/uploads/2015/09/1905_adele.jpg")
	
	'''Aretha Franklin'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=-aVCoKV6XpVJ8U1wNNOkbo6BzgCdf83m')
	addDir(addonString(30326).encode('utf-8'),list,17,"http://sandiegofreepress.org/wp-content/uploads/2013/01/ARETHA-FRANKLIN-QUEEN-OF-SOUL.jpg",addonString(30426).encode('utf-8'),'1',0,"http://img0.ndsstatic.com/wallpapers/54bd6b2fafd5e81b18a44a28a6cda97e_large.jpeg")
	
	'''Beyonce'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=arPDo5YMm5RA7XMeJtn5HFDdXPed4A-X')
	addDir(addonString(30302).encode('utf-8'),list,17,"http://factmag-images.s3.amazonaws.com/wp-content/uploads/2013/05/beyonce-5.13.20132.jpg",addonString(30402).encode('utf-8'),'1',0,"http://askkissy.com/wp-content/uploads/2016/02/image4.jpeg")
	
	'''Bob Marley'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLF76A601FD261FE55') 
	addDir(addonString(30322).encode('utf-8'),list,17,"http://imgc.allpostersimages.com/images/P-473-488-90/65/6544/ATK4100Z/posters/bob-marley-colors.jpg/300px-Bob-Marley-in-Concert_Zurich_05-30-80.jpg",addonString(30422).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/_KzaFxGME9o/maxresdefault.jpg")
	
	'''Bob Dylan'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL7B7E250ABE8B4E64&index=2&spfreload=1')
	addDir(addonString(30323).encode('utf-8'),list,17,"http://www.rockbandaide.com/wp-content/uploads/2014/02/Bob-Dylan-Times-are-Changing-C10113356.jpg",addonString(30423).encode('utf-8'),'1',0,"http://knownpeople.net/wp-content/uploads/b/bob-dylan-wallpapers.jpg")
	
	'''Britney Spears'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL595EC905D80443EB')
	addDir(addonString(30350).encode('utf-8'),list,17,"http://guardianlv.com/wp-content/uploads/2013/12/Britney-Spears-Hits-Vegas-With-Piece-of-Me-Concert-Series-e1388228163153.jpg",addonString(30450).encode('utf-8'),'1',0,"http://science-all.com/images/wallpapers/britney-spears-wallpaper/britney-spears-wallpaper-8.jpg")
	
	'''Celine Dion'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLVNmwycFozUGB6b6fKcldWyfmZR4RZIJj')
	addDir(addonString(30332).encode('utf-8'),list,17,"https://www.vegas.com/shows/concerts/celine-dion-las-vegas/lg_celine-dion-large-2.jpg",addonString(30432).encode('utf-8'),'1',0,"http://wallpapers55.com/wp-content/uploads/2013/11/hd-wallpaper-celine-dion.jpg")
	
	'''Christina Aguilera'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30307).encode('utf-8'),list,17,"http://www.billboard.com/files/styles/article_main_image/public/media/christina-aguilera_press-2013-650b.jpg",addonString(30407).encode('utf-8'),'1',0,"https://images6.alphacoders.com/342/342248.jpg")
	
	'''Coldplay'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLD88DB02A8CA3EBC2')
	addDir(addonString(30329).encode('utf-8'),list,17,"http://static.guim.co.uk/sys-images/Guardian/Pix/pictures/2011/10/12/1318414177419/Coldplay-007.jpg",addonString(30429).encode('utf-8'),'1',0,"http://worldversus.com/img/coldplay.jpg")
	
	'''David Bowie'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL4FA0D24F56BD0191')
	addDir(addonString(30351).encode('utf-8'),list,17,"https://wallpaperscraft.com/image/david_bowie_face_fist_sweater_look_3332_1920x1080.jpg",addonString(30451).encode('utf-8'),'1',0,"http://www.monstersandcritics.com/wp-content/uploads/2016/01/david-bowie-album-blackstar.jpg")
	
	'''Elton John'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLA910D381CD5AF74E')
	addDir(addonString(30352).encode('utf-8'),list,17,"http://i.huffpost.com/gen/2722330/images/o-ELTON-JOHN-facebook.jpg",addonString(30452).encode('utf-8'),'1',0,"http://hdwallpaperbackgrounds.net/wp-content/uploads/2015/09/Elton-John-HD-Wallpapers.jpg")
	
	'''Elvis Presley'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLVsyHu2yDLkzdYcDjz8yqw84CmcYZGCIt')
	addDir(addonString(30320).encode('utf-8'),list,17,"http://static.europosters.cz/image/750/plakatok/elvis-presley-portrait-i9038.jpg/375px-Elvis_Presley_promoting_Jailhouse_Rock.jpg",addonString(30420).encode('utf-8'),'1',0,"http://www.alux.com/wp-content/uploads/2015/06/070a67ca54831a9f02541f76a8c5ec71_large_21275600.jpeg")
	
	'''Eminem'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_ch=EminemVEVO')
	addDir(addonString(30309).encode('utf-8'),list,17,"http://static.gigwise.com/artists/best-bets-albums-eminem-650-430%20(1).jpg",addonString(30409).encode('utf-8'),'1',0,"http://thesource.com/wp-content/uploads/2016/03/eminem-5.jpg")
	
	'''Enrique Iglesias'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_ch=EnriqueIglesiasVEVO')
	addDir(addonString(30317).encode('utf-8'),list,17,"http://www.quoteauthors.com/wp-content/uploads/2015/10/enrique-iglesias.jpg",addonString(30417).encode('utf-8'),'1',0,"https://images8.alphacoders.com/421/421324.jpg")
	
	'''Eric Clapton'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLnTKYzbTaPq4yjmTe5CwzpRUvHlJspIO7')
	addDir(addonString(30324).encode('utf-8'),list,17,"http://rock.amazingradios.com/wp-content/uploads/2014/10/eric-clapton-9.jpg",addonString(30424).encode('utf-8'),'1',0,"https://ichef.bbci.co.uk/images/ic/1920x1080/p01hycb8.jpg")
	
	'''Jean Michel Jarre'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL0X6k9ILt02rs8SYwNfNxgGHTDzTA-eWI')
	addDir(addonString(30331).encode('utf-8'),list,17,"http://www.whale.to/c/zs107kz4jarre.jpg",addonString(30431).encode('utf-8'),'1',"electronic music", "http://assets.noisey.com/content-images/contentimage/71853/jmj-4.jpg")
	
	'''Jennifer Lopez'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLC9944199588E8EE8')
	addDir(addonString(30318).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Jennifer_Lopez_GLAAD_2014.jpg/375px-Jennifer_Lopez_GLAAD_2014.jpg",addonString(30418).encode('utf-8'),'1',0,"http://www.hitsync.net/wp-content/uploads/2016/04/WDF_2451822.jpg")
	
	'''Justin Bieber'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30330).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Believe_Tour_7%2C_2012.jpg/375px-Believe_Tour_7%2C_2012.jpg",addonString(30430).encode('utf-8'),'1',0,"http://deskbg.com/i/c/1920x1200/wpp/0/157/justin-bieber-desktop-background.jpg")
	
	'''Katy Perry'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_ch=KatyPerryVEVO')
	addDir(addonString(30319).encode('utf-8'),list,17,"https://i.ytimg.com/vi/CevxZvSJLk8/maxresdefault.jpg",addonString(30419).encode('utf-8'),'1',0,"http://fullhdpictures.com/wp-content/uploads/2015/05/Best-of-Katy-Perry-Wallpapers.jpg")
	
	'''Meghan Trainor'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_ch=MeghanTrainorVEVO')
	addDir(addonString(30321).encode('utf-8'),list,17,"http://www.rosh1.co.il/wp-content/uploads/2014/12/460792920-490x429.jpg",addonString(30421).encode('utf-8'),'1',0,"http://www.popologynow.com/wp-content/uploads/2016/05/Meghan-Trainor-Thats-What-She-Said.jpg")
	
	'''Michael Jackson'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL3CF35F99B7B4A227')
	addDir(addonString(30301).encode('utf-8'),list,17,"https://michaeljacksonisrael.files.wordpress.com/2013/05/69235_majkl-dzhekson_or_michael-jack21.jpg",addonString(30401).encode('utf-8'),'1',0,"http://www.rockfm.mx/rock_tv/lesdoit-michaeljackson.jpg")
	
	'''Maddona'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLOOBElWP-gj6hl7PQVcZak9FGri0ppeWG')
	addDir(addonString(30311).encode('utf-8'),list,17,"http://g04.a.alicdn.com/kf/HTB1jqmjIVXXXXbSapXXq6xXFXXX4/%D7%AA%D7%90%D7%A8%D7%99%D7%9A-%D7%94%D7%9E%D7%A1%D7%AA%D7%95%D7%A8%D7%99%D7%9F-%D7%A9%D7%97%D7%A7%D7%A0%D7%99%D7%AA-%D7%A7%D7%95%D7%9C%D7%A0%D7%95%D7%A2-%D7%9E%D7%93%D7%95%D7%A0%D7%94-ciccone-%D7%A4%D7%95%D7%A1%D7%98%D7%A8-%D7%A6%D7%99%D7%95%D7%A8-%D7%93%D7%A7%D7%95%D7%A8%D7%98%D7%99%D7%91%D7%99-%D7%9C%D7%91%D7%99%D7%AA-%D7%91%D7%93-%D7%9E%D7%A9%D7%99-%D7%94%D7%93%D7%A4%D7%A1%D7%94.jpg",addonString(30411).encode('utf-8'),'1',0,"http://weneedfun.com/wp-content/uploads/2015/10/Madonna-HD-Pictures-17.jpg")
	
	'''Mariah Carey'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLEB34410B67CCA932')
	addDir(addonString(30313).encode('utf-8'),list,17,"http://www.studentsoftheworld.info/sites/musique/img/2827_Maria_Carey_1.jpg",addonString(30413).encode('utf-8'),'1',0,"http://wallpaperswide.com/download/mariah_carey_2-wallpaper-1920x1080.jpg")
	
	'''Maroon 5'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_ch=Maroon5VEVO')
	addDir(addonString(30308).encode('utf-8'),list,17,"http://www.aaarena.com/assets/img/Concert_Maroon5.jpg",addonString(30408).encode('utf-8'),'1',0,"http://www.guitarfree.co.il/wp-content/uploads/8bc571dfd3347ae39c1002c81e32536a.jpg")
	
	'''Pharrell Williams'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_ch=PharrellWilliamsVEVO')
	addDir(addonString(30312).encode('utf-8'),list,17,"http://cdn.bleedingcool.net/wp-content/uploads/2013/10/Pharrell-Williams.jpg",addonString(30412).encode('utf-8'),'1',0,"http://content.acclaimmag.com/content/uploads/2016/04/1398788909Adi_Pharrell.jpg")
	
	'''Roy Orbison'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_ch=RoyOrbison')
	list.append('&youtube_pl=PLvPrczMM8gz3y1Iboy6CsZ432HjCWUQgR&index=15')
	addDir(addonString(30310).encode('utf-8'),list,17,"http://www.billboard.com/files/styles/promo_650/public/stylus/1077939-roy-orbison-617-409.jpg",addonString(30410).encode('utf-8'),'1',0,"https://fanart.tv/fanart/music/0bbbc496-c7b5-4b3f-bb6d-bd312827d6e5/artistbackground/orbison-roy-503635210f7d1.jpg")
	
	'''Rihanna'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL2DC5A0B189256D7D&index=4')
	addDir(addonString(30303).encode('utf-8'),list,17,"http://static1.1.sqspcdn.com/static/f/610086/15180915/1321583897117/Rihanna.jpg?token=kZt1lYEul%2FfTahdORTKehFd28NI%3D/site1/20091127/0023ae9885da0c7990e10d.jpg&pw=200",addonString(30403).encode('utf-8'),'1',0,"http://xdesktopwallpapers.com/wp-content/uploads/2011/08/Rihanna-Pink-Lips-N-Brown-Eyes-Face-Closeups.jpg")
	
	'''Sam Smith'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30333).encode('utf-8'),list,17,"https://yt3.ggpht.com/-9z_bFRPDMYQ/AAAAAAAAAAI/AAAAAAAAAAA/czjhAF4k4aw/s100-c-k-no/photo.jpg",addonString(30433).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/lf3W5YtcyaY/maxresdefault.jpg")
	
	'''Taylor Swift'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_ch=TaylorSwiftVEVO')
	addDir(addonString(30304).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/he/5/58/Taylor_Swift_-_Taylor_Swift_Album_Cover.png",addonString(30404).encode('utf-8'),'1',0,"http://hdcoolwallpapers.com/wp-content/uploads/2015/03/Taylor-Swift-Wallpapers-HD-041.jpg")
	
	'''Usher'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_ch=UsherVEVO')
	addDir(addonString(30315).encode('utf-8'),list,17,"http://www.usherdaily.com/wp-content/uploads/2015/02/usher-2014-cover-bb36-01-650.jpg",addonString(30415).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/xbkUdPotU3A/maxresdefault.jpg")
	
	'''Whitney Houston'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL201BB89398FE5675')
	addDir(addonString(30314).encode('utf-8'),list,17,"http://img2.timeinc.net/people/i/2012/specials/yearend/obits/whitney-houston-1435.jpg",addonString(30414).encode('utf-8'),'1',0,"https://content2.promiflash.de/article-images/video_1080/whitney-houston-ganz-in-schwarz.jpg")

	CATEGORIES11101A(name, iconimage, desc, fanart) #דף הבא
	
def CATEGORIES11102(name, iconimage, desc, fanart):
	'''------------------------------
	---Foreign-Karaoke---------------
	------------------------------'''
	background = 112
	commonsearch = 'commonsearch112'
	
	CATEGORIES_RANDOM(background,fanart)
	'''חיפוש'''
	addDir(localize(137),'karaoke',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(32416).encode('utf-8') % (localize(13327)),'1',0,fanart)
	
	CATEGORIES11102Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
		
	'''Adele'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30327).encode('utf-8'),list,17,'http://cdn.cultofmac.com/wp-content/uploads/2015/11/adele-third-album-25.jpg',addonString(30427).encode('utf-8'),'1',0,"http://yesofcorsa.com/wp-content/uploads/2015/09/1905_adele.jpg")
	
	'''Aretha Franklin'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30326).encode('utf-8'),list,17,"http://sandiegofreepress.org/wp-content/uploads/2013/01/ARETHA-FRANKLIN-QUEEN-OF-SOUL.jpg",addonString(30426).encode('utf-8'),'1',0,"http://img0.ndsstatic.com/wallpapers/54bd6b2fafd5e81b18a44a28a6cda97e_large.jpeg")
	
	'''Beyonce'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30302).encode('utf-8'),list,17,"http://factmag-images.s3.amazonaws.com/wp-content/uploads/2013/05/beyonce-5.13.20132.jpg",addonString(30402).encode('utf-8'),'1',0,"http://askkissy.com/wp-content/uploads/2016/02/image4.jpeg")
	
	'''Bob Marley'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30322).encode('utf-8'),list,17,"http://imgc.allpostersimages.com/images/P-473-488-90/65/6544/ATK4100Z/posters/bob-marley-colors.jpg/300px-Bob-Marley-in-Concert_Zurich_05-30-80.jpg",addonString(30422).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/_KzaFxGME9o/maxresdefault.jpg")
	
	'''Bob Dylan'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30323).encode('utf-8'),list,17,"http://www.rockbandaide.com/wp-content/uploads/2014/02/Bob-Dylan-Times-are-Changing-C10113356.jpg",addonString(30423).encode('utf-8'),'1',0,"http://knownpeople.net/wp-content/uploads/b/bob-dylan-wallpapers.jpg")
	
	'''Britney Spears'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30350).encode('utf-8'),list,17,"http://guardianlv.com/wp-content/uploads/2013/12/Britney-Spears-Hits-Vegas-With-Piece-of-Me-Concert-Series-e1388228163153.jpg",addonString(30450).encode('utf-8'),'1',0,"http://science-all.com/images/wallpapers/britney-spears-wallpaper/britney-spears-wallpaper-8.jpg")
	
	'''Celine Dion'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30332).encode('utf-8'),list,17,"https://www.vegas.com/shows/concerts/celine-dion-las-vegas/lg_celine-dion-large-2.jpg",addonString(30432).encode('utf-8'),'1',0,"http://wallpapers55.com/wp-content/uploads/2013/11/hd-wallpaper-celine-dion.jpg")
	
	'''Christina Aguilera'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30307).encode('utf-8'),list,17,"http://www.billboard.com/files/styles/article_main_image/public/media/christina-aguilera_press-2013-650b.jpg",addonString(30407).encode('utf-8'),'1',0,"https://images6.alphacoders.com/342/342248.jpg")
	
	'''Coldplay'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30329).encode('utf-8'),list,17,"http://static.guim.co.uk/sys-images/Guardian/Pix/pictures/2011/10/12/1318414177419/Coldplay-007.jpg",addonString(30429).encode('utf-8'),'1',0,"http://worldversus.com/img/coldplay.jpg")
	
	'''David Bowie'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30351).encode('utf-8'),list,17,"https://wallpaperscraft.com/image/david_bowie_face_fist_sweater_look_3332_1920x1080.jpg",addonString(30451).encode('utf-8'),'1',0,getAddonFanart(background, custom="https://wallpaperscraft.com/image/david_bowie_face_fist_sweater_look_3332_1920x1080.jpg")
	
	'''Elton John'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30352).encode('utf-8'),list,17,"http://i.huffpost.com/gen/2722330/images/o-ELTON-JOHN-facebook.jpg",addonString(30452).encode('utf-8'),'1',0,"http://hdwallpaperbackgrounds.net/wp-content/uploads/2015/09/Elton-John-HD-Wallpapers.jpg")
	
	'''Elvis Presley'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30320).encode('utf-8'),list,17,"http://static.europosters.cz/image/750/plakatok/elvis-presley-portrait-i9038.jpg/375px-Elvis_Presley_promoting_Jailhouse_Rock.jpg",addonString(30420).encode('utf-8'),'1',0,"http://www.alux.com/wp-content/uploads/2015/06/070a67ca54831a9f02541f76a8c5ec71_large_21275600.jpeg")
	
	'''Eminem'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL7C428AEA0ABF7560')
	list.append('&youtube_pl=PLkvGbaSME8vLpiGZHSLS8X-nIADHE8MRf')
	addDir(addonString(30309).encode('utf-8'),list,17,"http://static.gigwise.com/artists/best-bets-albums-eminem-650-430%20(1).jpg",addonString(30409).encode('utf-8'),'1',0,"http://thesource.com/wp-content/uploads/2016/03/eminem-5.jpg")

	'''Enrique Iglesias'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30317).encode('utf-8'),list,17,"http://www.quoteauthors.com/wp-content/uploads/2015/10/enrique-iglesias.jpg",addonString(30417).encode('utf-8'),'1',0,"https://images8.alphacoders.com/421/421324.jpg")
	
	'''Eric Clapton'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30324).encode('utf-8'),list,17,"http://rock.amazingradios.com/wp-content/uploads/2014/10/eric-clapton-9.jpg",addonString(30424).encode('utf-8'),'1',0,"https://ichef.bbci.co.uk/images/ic/1920x1080/p01hycb8.jpg")
	
	'''Jean Michel Jarre'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30331).encode('utf-8'),list,17,"http://www.whale.to/c/zs107kz4jarre.jpg",addonString(30431).encode('utf-8'),'1',"electronic music", "http://assets.noisey.com/content-images/contentimage/71853/jmj-4.jpg")
	
	'''Jennifer Lopez'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30318).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Jennifer_Lopez_GLAAD_2014.jpg/375px-Jennifer_Lopez_GLAAD_2014.jpg",addonString(30418).encode('utf-8'),'1',0,"http://www.hitsync.net/wp-content/uploads/2016/04/WDF_2451822.jpg")
	
	'''Justin Bieber'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30330).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Believe_Tour_7%2C_2012.jpg/375px-Believe_Tour_7%2C_2012.jpg",addonString(30430).encode('utf-8'),'1',0,"http://deskbg.com/i/c/1920x1200/wpp/0/157/justin-bieber-desktop-background.jpg")
	
	'''Katy Perry'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30319).encode('utf-8'),list,17,"https://i.ytimg.com/vi/CevxZvSJLk8/maxresdefault.jpg",addonString(30419).encode('utf-8'),'1',0,"http://fullhdpictures.com/wp-content/uploads/2015/05/Best-of-Katy-Perry-Wallpapers.jpg")
	
	'''Meghan Trainor'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30321).encode('utf-8'),list,17,"http://www.rosh1.co.il/wp-content/uploads/2014/12/460792920-490x429.jpg",addonString(30421).encode('utf-8'),'1',0,"http://www.popologynow.com/wp-content/uploads/2016/05/Meghan-Trainor-Thats-What-She-Said.jpg")
	
	'''Michael Jackson'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL3CF35F99B7B4A227')
	addDir(addonString(30301).encode('utf-8'),list,17,"https://michaeljacksonisrael.files.wordpress.com/2013/05/69235_majkl-dzhekson_or_michael-jack21.jpg",addonString(30401).encode('utf-8'),'1',0,"http://www.rockfm.mx/rock_tv/lesdoit-michaeljackson.jpg")
	
	'''Maddona'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLOOBElWP-gj6hl7PQVcZak9FGri0ppeWG')
	addDir(addonString(30311).encode('utf-8'),list,17,"http://g04.a.alicdn.com/kf/HTB1jqmjIVXXXXbSapXXq6xXFXXX4/%D7%AA%D7%90%D7%A8%D7%99%D7%9A-%D7%94%D7%9E%D7%A1%D7%AA%D7%95%D7%A8%D7%99%D7%9F-%D7%A9%D7%97%D7%A7%D7%A0%D7%99%D7%AA-%D7%A7%D7%95%D7%9C%D7%A0%D7%95%D7%A2-%D7%9E%D7%93%D7%95%D7%A0%D7%94-ciccone-%D7%A4%D7%95%D7%A1%D7%98%D7%A8-%D7%A6%D7%99%D7%95%D7%A8-%D7%93%D7%A7%D7%95%D7%A8%D7%98%D7%99%D7%91%D7%99-%D7%9C%D7%91%D7%99%D7%AA-%D7%91%D7%93-%D7%9E%D7%A9%D7%99-%D7%94%D7%93%D7%A4%D7%A1%D7%94.jpg",addonString(30411).encode('utf-8'),'1',0,"http://weneedfun.com/wp-content/uploads/2015/10/Madonna-HD-Pictures-17.jpg")
	
	'''Mariah Carey'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLEB34410B67CCA932')
	addDir(addonString(30313).encode('utf-8'),list,17,"http://www.studentsoftheworld.info/sites/musique/img/2827_Maria_Carey_1.jpg",addonString(30413).encode('utf-8'),'1',0,"http://wallpaperswide.com/download/mariah_carey_2-wallpaper-1920x1080.jpg")
	
	'''Maroon 5'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLAEq5ujOZ71rI-rJhF2OqUZWmjxpo4I9L')
	list.append('&youtube_pl=PLnpWcMv6bu2UoS9jy7uRjvPWRrTe6bZQZ')
	addDir(addonString(30308).encode('utf-8'),list,17,"http://www.aaarena.com/assets/img/Concert_Maroon5.jpg",addonString(30408).encode('utf-8'),'1',0,"http://www.guitarfree.co.il/wp-content/uploads/8bc571dfd3347ae39c1002c81e32536a.jpg")
	
	'''Pharrell Williams'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLIo8l2xEQymvfj8uwrw2TNbVImihLzLiH')
	addDir(addonString(30312).encode('utf-8'),list,17,"http://cdn.bleedingcool.net/wp-content/uploads/2013/10/Pharrell-Williams.jpg",addonString(30412).encode('utf-8'),'1',0,"http://content.acclaimmag.com/content/uploads/2016/04/1398788909Adi_Pharrell.jpg")
	
	'''Roy Orbison'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30310).encode('utf-8'),list,17,"http://www.billboard.com/files/styles/promo_650/public/stylus/1077939-roy-orbison-617-409.jpg",addonString(30410).encode('utf-8'),'1',0,"https://fanart.tv/fanart/music/0bbbc496-c7b5-4b3f-bb6d-bd312827d6e5/artistbackground/orbison-roy-503635210f7d1.jpg")
	
	'''Rihanna'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30303).encode('utf-8'),list,17,"http://static1.1.sqspcdn.com/static/f/610086/15180915/1321583897117/Rihanna.jpg?token=kZt1lYEul%2FfTahdORTKehFd28NI%3D/site1/20091127/0023ae9885da0c7990e10d.jpg&pw=200",addonString(30403).encode('utf-8'),'1',0,"http://xdesktopwallpapers.com/wp-content/uploads/2011/08/Rihanna-Pink-Lips-N-Brown-Eyes-Face-Closeups.jpg")
	
	'''Sam Smith'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30333).encode('utf-8'),list,17,"https://yt3.ggpht.com/-9z_bFRPDMYQ/AAAAAAAAAAI/AAAAAAAAAAA/czjhAF4k4aw/s100-c-k-no/photo.jpg",addonString(30433).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/lf3W5YtcyaY/maxresdefault.jpg")
	
	'''Taylor Swift'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30304).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/he/5/58/Taylor_Swift_-_Taylor_Swift_Album_Cover.png",addonString(30404).encode('utf-8'),'1',0,"http://hdcoolwallpapers.com/wp-content/uploads/2015/03/Taylor-Swift-Wallpapers-HD-041.jpg")
	
	'''Usher'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30315).encode('utf-8'),list,17,"http://www.usherdaily.com/wp-content/uploads/2015/02/usher-2014-cover-bb36-01-650.jpg",addonString(30415).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/xbkUdPotU3A/maxresdefault.jpg")
	
	'''Whitney Houston'''
	list = []
	list.append('&youtube_pl=PL201BB89398FE5675')
	addDir(addonString(30314).encode('utf-8'),list,17,"http://img2.timeinc.net/people/i/2012/specials/yearend/obits/whitney-houston-1435.jpg",addonString(30414).encode('utf-8'),'1',0,"https://content2.promiflash.de/article-images/video_1080/whitney-houston-ganz-in-schwarz.jpg")
	
	CATEGORIES11102A(name, iconimage, desc, fanart) #דף הבא
	
def CATEGORIES11104(name, iconimage, desc, fanart):
	'''------------------------------
	---Foreign-Liveshows-------------
	------------------------------'''
	background = 114
	commonsearch = 'commonsearch114'
	
	CATEGORIES_RANDOM(background,fanart)
	'''חיפוש'''
	addDir(localize(137),'liveshow',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(32416).encode('utf-8') % (addonString(30020).encode('utf-8')),'1',0,fanart)
	
	CATEGORIES11104Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
	'''Adele'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30327).encode('utf-8'),list,17,'http://cdn.cultofmac.com/wp-content/uploads/2015/11/adele-third-album-25.jpg',addonString(30427).encode('utf-8'),'1',0,"http://yesofcorsa.com/wp-content/uploads/2015/09/1905_adele.jpg")
	
	'''Aretha Franklin'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=a3raW4rt2fE')
	list.append('&youtube_id=y0xZsepl4Is')
	list.append('&youtube_id=CbmB2nXJRDM')
	addDir(addonString(30326).encode('utf-8'),list,17,"http://sandiegofreepress.org/wp-content/uploads/2013/01/ARETHA-FRANKLIN-QUEEN-OF-SOUL.jpg",addonString(30426).encode('utf-8'),'1',0,"http://img0.ndsstatic.com/wallpapers/54bd6b2fafd5e81b18a44a28a6cda97e_large.jpeg")
	
	'''Beyonce'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30302).encode('utf-8'),list,17,"http://factmag-images.s3.amazonaws.com/wp-content/uploads/2013/05/beyonce-5.13.20132.jpg",addonString(30402).encode('utf-8'),'1',0,"http://askkissy.com/wp-content/uploads/2016/02/image4.jpeg")
	
	'''Bob Marley'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30322).encode('utf-8'),list,17,"http://imgc.allpostersimages.com/images/P-473-488-90/65/6544/ATK4100Z/posters/bob-marley-colors.jpg/300px-Bob-Marley-in-Concert_Zurich_05-30-80.jpg",addonString(30422).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/_KzaFxGME9o/maxresdefault.jpg")
	
	'''Bob Dylan'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30323).encode('utf-8'),list,17,"http://www.rockbandaide.com/wp-content/uploads/2014/02/Bob-Dylan-Times-are-Changing-C10113356.jpg",addonString(30423).encode('utf-8'),'1',0,"http://knownpeople.net/wp-content/uploads/b/bob-dylan-wallpapers.jpg")

	'''Britney Spears'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30350).encode('utf-8'),list,17,"http://guardianlv.com/wp-content/uploads/2013/12/Britney-Spears-Hits-Vegas-With-Piece-of-Me-Concert-Series-e1388228163153.jpg",addonString(30450).encode('utf-8'),'1',0,"http://science-all.com/images/wallpapers/britney-spears-wallpaper/britney-spears-wallpaper-8.jpg")
	
	'''Celine Dion'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30332).encode('utf-8'),list,17,"https://www.vegas.com/shows/concerts/celine-dion-las-vegas/lg_celine-dion-large-2.jpg",addonString(30432).encode('utf-8'),'1',0,"http://wallpapers55.com/wp-content/uploads/2013/11/hd-wallpaper-celine-dion.jpg")
	
	'''Christina Aguilera'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30307).encode('utf-8'),list,17,"http://www.billboard.com/files/styles/article_main_image/public/media/christina-aguilera_press-2013-650b.jpg",addonString(30407).encode('utf-8'),'1',0,"https://images6.alphacoders.com/342/342248.jpg")
	
	'''Coldplay'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=vMAyzVr_fZI')
	addDir(addonString(30329).encode('utf-8'),list,17,"http://static.guim.co.uk/sys-images/Guardian/Pix/pictures/2011/10/12/1318414177419/Coldplay-007.jpg",addonString(30429).encode('utf-8'),'1',0,"http://worldversus.com/img/coldplay.jpg")
	
	'''David Bowie'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30351).encode('utf-8'),list,17,"https://wallpaperscraft.com/image/david_bowie_face_fist_sweater_look_3332_1920x1080.jpg",addonString(30451).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://www.monstersandcritics.com/wp-content/uploads/2016/01/david-bowie-album-blackstar.jpg")
	
	'''Elton John'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=9_5UFmJ7YhM')
	list.append('&youtube_id=9_3WKNlZg-qr8')
	addDir(addonString(30352).encode('utf-8'),list,17,"http://i.huffpost.com/gen/2722330/images/o-ELTON-JOHN-facebook.jpg",addonString(30452).encode('utf-8'),'1',0,"http://hdwallpaperbackgrounds.net/wp-content/uploads/2015/09/Elton-John-HD-Wallpapers.jpg")
	
	'''Elvis Presley'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30320).encode('utf-8'),list,17,"http://static.europosters.cz/image/750/plakatok/elvis-presley-portrait-i9038.jpg/375px-Elvis_Presley_promoting_Jailhouse_Rock.jpg",addonString(30420).encode('utf-8'),'1',0,"http://www.alux.com/wp-content/uploads/2015/06/070a67ca54831a9f02541f76a8c5ec71_large_21275600.jpeg")
	
	'''Eminem'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=ldWvm-ZqKaY')
	list.append('&youtube_id=Dn3qfGz_Yq8')
	list.append('&youtube_id=cc0YH5JdmKc')
	list.append('&youtube_id=cKY7xpCZozE')
	list.append('&youtube_id=7vAmygdfya0')
	list.append('&youtube_id=trz0V6Fkb9I')
	list.append('&youtube_id=-DWiECMKLDE')
	list.append('&youtube_id=7LbT4MlfcP4')
	list.append('&youtube_id=Lu1s83soD1I')
	list.append('&youtube_id=clpxUD2bbWQ')
	list.append('&youtube_id=8xeXEalVlQ4')
	addDir(addonString(30309).encode('utf-8'),list,17,"http://static.gigwise.com/artists/best-bets-albums-eminem-650-430%20(1).jpg",addonString(30409).encode('utf-8'),'1',0,"http://thesource.com/wp-content/uploads/2016/03/eminem-5.jpg")

	'''Enrique Iglesias'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30317).encode('utf-8'),list,17,"http://www.quoteauthors.com/wp-content/uploads/2015/10/enrique-iglesias.jpg",addonString(30417).encode('utf-8'),'1',0,"https://images8.alphacoders.com/421/421324.jpg")
	
	'''Eric Clapton'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30324).encode('utf-8'),list,17,"http://rock.amazingradios.com/wp-content/uploads/2014/10/eric-clapton-9.jpg",addonString(30424).encode('utf-8'),'1',0,"https://ichef.bbci.co.uk/images/ic/1920x1080/p01hycb8.jpg")
	
	'''Jean Michel Jarre'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30331).encode('utf-8'),list,17,"http://www.whale.to/c/zs107kz4jarre.jpg",addonString(30431).encode('utf-8'),'1',"electronic music", "http://assets.noisey.com/content-images/contentimage/71853/jmj-4.jpg")
	
	'''Jennifer Lopez'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30318).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Jennifer_Lopez_GLAAD_2014.jpg/375px-Jennifer_Lopez_GLAAD_2014.jpg",addonString(30418).encode('utf-8'),'1',0,"http://www.hitsync.net/wp-content/uploads/2016/04/WDF_2451822.jpg")
	
	'''Justin Bieber'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30330).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Believe_Tour_7%2C_2012.jpg/375px-Believe_Tour_7%2C_2012.jpg",addonString(30430).encode('utf-8'),'1',0,"http://deskbg.com/i/c/1920x1200/wpp/0/157/justin-bieber-desktop-background.jpg")
	
	'''Katy Perry'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=P65_WpalmdA')
	list.append('&youtube_id=-1cyCmUdDNQ')
	list.append('&youtube_id=RWmRIPoSj1A')
	list.append('&youtube_id=lFgtmfaUmvU')
	list.append('&youtube_id=6SmyCkJvh9Y')
	addDir(addonString(30319).encode('utf-8'),list,17,"https://i.ytimg.com/vi/CevxZvSJLk8/maxresdefault.jpg",addonString(30419).encode('utf-8'),'1',0,"http://fullhdpictures.com/wp-content/uploads/2015/05/Best-of-Katy-Perry-Wallpapers.jpg")
	
	'''Meghan Trainor'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=GJ6cU-ZpHbU')
	list.append('&youtube_id=ewaQgopjitg')
	list.append('&youtube_id=gp4Pe0dqN8E')
	list.append('&youtube_id=c-cRRs8uYgc')
	addDir(addonString(30321).encode('utf-8'),list,17,"http://www.rosh1.co.il/wp-content/uploads/2014/12/460792920-490x429.jpg",addonString(30421).encode('utf-8'),'1',0,"http://www.popologynow.com/wp-content/uploads/2016/05/Meghan-Trainor-Thats-What-She-Said.jpg")
	
	'''Michael Jackson'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL3CF35F99B7B4A227')
	addDir(addonString(30301).encode('utf-8'),list,17,"https://michaeljacksonisrael.files.wordpress.com/2013/05/69235_majkl-dzhekson_or_michael-jack21.jpg",addonString(30401).encode('utf-8'),'1',0,"http://www.rockfm.mx/rock_tv/lesdoit-michaeljackson.jpg")
	
	'''Maddona'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLOOBElWP-gj6hl7PQVcZak9FGri0ppeWG')
	list.append('&youtube_id=aiuB_e2QYb8')
	list.append('&youtube_id=49BR8thSLIc')
	list.append('&youtube_id=tph7mf068o4')
	list.append('&youtube_id=bLZjDPhvqpM')
	list.append('&youtube_id=Y4oCBZV8SHA')
	list.append('&youtube_id=IR68GRYiPl4')
	list.append('&youtube_id=liXbh4lZRmk')
	list.append('&youtube_id=WfGjVnwavXk')
	list.append('&youtube_id=i16PhTEKinA')
	list.append('&youtube_id=72II5X6uceo')
	list.append('&youtube_id=8eGtHXjRuO8')
	addDir(addonString(30311).encode('utf-8'),list,17,"http://g04.a.alicdn.com/kf/HTB1jqmjIVXXXXbSapXXq6xXFXXX4/%D7%AA%D7%90%D7%A8%D7%99%D7%9A-%D7%94%D7%9E%D7%A1%D7%AA%D7%95%D7%A8%D7%99%D7%9F-%D7%A9%D7%97%D7%A7%D7%A0%D7%99%D7%AA-%D7%A7%D7%95%D7%9C%D7%A0%D7%95%D7%A2-%D7%9E%D7%93%D7%95%D7%A0%D7%94-ciccone-%D7%A4%D7%95%D7%A1%D7%98%D7%A8-%D7%A6%D7%99%D7%95%D7%A8-%D7%93%D7%A7%D7%95%D7%A8%D7%98%D7%99%D7%91%D7%99-%D7%9C%D7%91%D7%99%D7%AA-%D7%91%D7%93-%D7%9E%D7%A9%D7%99-%D7%94%D7%93%D7%A4%D7%A1%D7%94.jpg",addonString(30411).encode('utf-8'),'1',0,"http://weneedfun.com/wp-content/uploads/2015/10/Madonna-HD-Pictures-17.jpg")
	
	'''Mariah Carey'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLEB34410B67CCA932')
	list.append('&youtube_pl=PLW86BSRZLdyoLMixcdANNKKQGYI6cAxUd')
	list.append('&youtube_id=fTtrc7Zmi7Q')
	list.append('&youtube_id=zyh87AZ4s_c')
	list.append('&youtube_id=7RIk7LKLNSI')
	list.append('&youtube_id=hSfOMsbKk2w')
	addDir(addonString(30313).encode('utf-8'),list,17,"http://www.studentsoftheworld.info/sites/musique/img/2827_Maria_Carey_1.jpg",addonString(30413).encode('utf-8'),'1',0,"http://wallpaperswide.com/download/mariah_carey_2-wallpaper-1920x1080.jpg")
	
	'''Maroon 5'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=C0PqR03HjW4')
	list.append('&youtube_id=yrnrQDZb2dY')
	list.append('&youtube_id=UbQll-N3AjA')
	list.append('&youtube_id=_qCrV5lmpQ0')
	list.append('&youtube_id=HqEpvbtoJec')
	list.append('&youtube_id=oAABDqaIxNk')
	list.append('&youtube_id=JlIsaeekv9E')
	addDir(addonString(30308).encode('utf-8'),list,17,"http://www.aaarena.com/assets/img/Concert_Maroon5.jpg",addonString(30408).encode('utf-8'),'1',0,"http://www.guitarfree.co.il/wp-content/uploads/8bc571dfd3347ae39c1002c81e32536a.jpg")
	
	'''Pharrell Williams'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=mISFzxi1kE0')
	list.append('&youtube_id=ALKKJ0o_ID8')
	list.append('&youtube_id=pI3yse4zK_M')
	list.append('&youtube_id=DB6Y-9e6pkI')
	list.append('&youtube_id=AQ4uaqyzQ_M')
	list.append('&youtube_id=oDEFegMpcYE')
	addDir(addonString(30312).encode('utf-8'),list,17,"http://cdn.bleedingcool.net/wp-content/uploads/2013/10/Pharrell-Williams.jpg",addonString(30412).encode('utf-8'),'1',0,"http://content.acclaimmag.com/content/uploads/2016/04/1398788909Adi_Pharrell.jpg")
	
	'''Roy Orbison'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=uAkNGdBTDQ4')
	list.append('&youtube_id=eV9GxtDao9g')
	list.append('&youtube_id=Fb6luT4NNJU')
	list.append('&youtube_id=9tZXIok6OF8')
	list.append('&youtube_id=pra6ezRMejg')
	list.append('&youtube_id=kkUNfpV8WUc')
	addDir(addonString(30310).encode('utf-8'),list,17,"http://www.billboard.com/files/styles/promo_650/public/stylus/1077939-roy-orbison-617-409.jpg",addonString(30410).encode('utf-8'),'1',0,"https://fanart.tv/fanart/music/0bbbc496-c7b5-4b3f-bb6d-bd312827d6e5/artistbackground/orbison-roy-503635210f7d1.jpg")
	
	'''Rihanna'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30303).encode('utf-8'),list,17,"http://static1.1.sqspcdn.com/static/f/610086/15180915/1321583897117/Rihanna.jpg?token=kZt1lYEul%2FfTahdORTKehFd28NI%3D/site1/20091127/0023ae9885da0c7990e10d.jpg&pw=200",addonString(30403).encode('utf-8'),'1',0,"http://xdesktopwallpapers.com/wp-content/uploads/2011/08/Rihanna-Pink-Lips-N-Brown-Eyes-Face-Closeups.jpg")
	
	'''Sam Smith'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30333).encode('utf-8'),list,17,"https://yt3.ggpht.com/-9z_bFRPDMYQ/AAAAAAAAAAI/AAAAAAAAAAA/czjhAF4k4aw/s100-c-k-no/photo.jpg",addonString(30433).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/lf3W5YtcyaY/maxresdefault.jpg")
	
	'''Taylor Swift'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30304).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/he/5/58/Taylor_Swift_-_Taylor_Swift_Album_Cover.png",addonString(30404).encode('utf-8'),'1',0,"http://hdcoolwallpapers.com/wp-content/uploads/2015/03/Taylor-Swift-Wallpapers-HD-041.jpg")
	
	'''Usher'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30315).encode('utf-8'),list,17,"http://www.usherdaily.com/wp-content/uploads/2015/02/usher-2014-cover-bb36-01-650.jpg",addonString(30415).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/xbkUdPotU3A/maxresdefault.jpg")

	'''Whitney Houston'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL201BB89398FE5675')
	addDir(addonString(30314).encode('utf-8'),list,17,"http://img2.timeinc.net/people/i/2012/specials/yearend/obits/whitney-houston-1435.jpg",addonString(30414).encode('utf-8'),'1',0,"https://content2.promiflash.de/article-images/video_1080/whitney-houston-ganz-in-schwarz.jpg")
	
	CATEGORIES11104A(name, iconimage, desc, fanart) #דף הבא
	
def CATEGORIES11105(name, iconimage, desc, fanart):
	'''------------------------------
	---Foregin-Djs-------------------
	------------------------------'''
	background = 115
	commonsearch = 'commonsearch115'
	
	CATEGORIES_RANDOM(background,fanart)
	CATEGORIES11105Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
	'''Afrojack'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30508).encode('utf-8'),list,17,"http://assets.rollingstone.com/assets/images/video/afrojack-pays-tribute-to-mentor-david-guetta-20131023/101613-afrojack-623-1381937652.jpg",addonString(30509).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/FA4p6buNHEY/maxresdefault.jpg")
	
	'''Armin Van Buuren'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30510).encode('utf-8'),list,17,"https://s3.amazonaws.com/webassets.ticketmob.com/ES/images/comedians/Armin-Van-Buuren-1.jpg",addonString(30511).encode('utf-8'),'1',0,"http://wallpaperbeta.com/wallpaper/armin_van_buuren_dj_man_hd-wallpaper-380351.jpg")
	
	'''Calvin Harris'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30516).encode('utf-8'),list,17,"http://www.billboard.com/files/styles/article_main_image/public/media/calvin-harris-press-gavin-bond-2015-billboard-650.jpg",addonString(30517).encode('utf-8'),'1',0,"https://fanart.tv/fanart/music/8dd98bdc-80ec-4e93-8509-2f46bafc09a7/artistbackground/harris-calvin-549a3f22a389c.jpg")
	
	'''Deadmau5'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30512).encode('utf-8'),list,17,"http://assets.rollingstone.com/assets/2014/article/deadmau5-replies-to-arcade-fires-anti-edm-jab-whats-your-problem-20140424/15140/_original/1035x702-20140424-deadmau5-x1800-1398358641.jpg",addonString(30513).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/f_1qLR1ns3w/maxresdefault.jpg")
	
	'''Hardwell'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30502).encode('utf-8'),list,17,"https://upload.wikimedia.org/wikipedia/commons/9/9b/Hardwell.jpg",addonString(30503).encode('utf-8'),'1',0,"https://fanart.tv/fanart/music/170d6637-36e0-49dd-a225-c4fd5b77a285/artistbackground/hardwell-52572f7f6e752.jpg")
	
	'''Martin Garrix'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30506).encode('utf-8'),list,17,"http://cdn.wegotthiscovered.com/wp-content/uploads/Garrix_Martin.jpg",addonString(30507).encode('utf-8'),'1',0,"https://images2.alphacoders.com/552/552649.jpg")
	
	'''Nick Rotteveel'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30506).encode('utf-8'),list,17,"http://cdn.wegotthiscovered.com/wp-content/uploads/Garrix_Martin.jpg",addonString(30507).encode('utf-8'),'1',0,"https://images2.alphacoders.com/552/552649.jpg")
	
	'''Skrillex'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30504).encode('utf-8'),list,17,"https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Skrillex.jpg/800px-Skrillex.jpg",addonString(30505).encode('utf-8'),'1',0,"https://wallpaperscraft.com/image/skrillex_glasses_haircut_shirt_look_7828_1920x1080.jpg")
	
	'''Steve Aoki'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30514).encode('utf-8'),list,17,"https://pbs.twimg.com/profile_images/614130977812684800/i-ivLi_n.png",addonString(30515).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/1b4WZtfkFZQ/maxresdefault.jpg")
	
	'''Tiësto'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(30500).encode('utf-8'),list,17,"https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/DJ_Tiesto2005.jpg/800px-DJ_Tiesto2005.jpg",addonString(30501).encode('utf-8'),'1',0,"http://www.shauntmax30.com/data/out/42/1308824-ruisufang-music-tiesto.jpg")
	
	CATEGORIES11105A(name, iconimage, desc, fanart) #דף הבא

def CATEGORIES114(name, iconimage, desc, fanart):
	'''תצוגות אופנה'''
	background = 114
	commonsearch = 'commonsearch114'
	
	CATEGORIES_RANDOM(background,fanart)
	CATEGORIES114Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
	'''Victoria Secret'''
	list = []
	list.append('&youtube_id=yv1CwJjSr7U') #2003
	list.append('&youtube_id=hQP71fV1N6Q') #2005-7-8
	list.append('&youtube_id=B17x7_9lAHw') #2006
	list.append('&youtube_id=7BJIsuX2HzU') #2007
	list.append('&youtube_id=_TmXwQxADgc') #2009
	list.append('&youtube_id=COvFvxOnd_0') #2010
	list.append('&youtube_id=N-Or4pxF64I') #2011
	list.append('&youtube_id=bYNhMnmraUE') #2011-2013
	list.append('&youtube_id=ljTQf5qcDh8') #2013
	list.append('&youtube_id=fpMo-aLnEEc') #2013
	list.append('&youtube_id=B8EMextFa5k') #2014
	list.append('&youtube_id=BjIaEwlnQz4') #2014
	list.append('&youtube_id=J3JN0LZB6hk') #2015
	list.append('&youtube_id=dWut7QA7jX8') #2015-2016
	list.append('&youtube_id=hmhZJg6KqSs') #2016
	list.append('&youtube_id=86mF928ZgFs') #2016
	list.append('&youtube_id=0rj0cFRvowU') #2016
	list.append('&youtube_id=0GNVS68g52Q') #2016
	list.append('&youtube_id=KffZEnYEK2s') #2016
	list.append('&youtube_id=hkgSTk0_DjM') #2016
	list.append('&youtube_id=TER4Mc1tVzQ') #2015
	list.append('&youtube_id=Vq9jmchquwQ') #2016-17
	addDir(addonString(30900).encode('utf-8'),list,17,"https://pbs.twimg.com/profile_images/542675764026429440/gPXHFroZ.png",addonString(30901).encode('utf-8'),'1',0,"https://s-media-cache-ak0.pinimg.com/originals/3f/be/f1/3fbef1cae14dea30c181f1f008839a1d.jpg")
	
	'''Gucci'''
	list = []
	list.append('&youtube_id=KpKUmZcUKRA') #2017
	list.append('&youtube_id=Cioa-jes2Ls') #2016
	list.append('&youtube_id=CZUJD5UdVzU') #
	list.append('&youtube_id=YucJfazpfoU') #
	list.append('&youtube_id=eZXHUBjcOVk') #
	addDir(addonString(30902).encode('utf-8'),list,17,"https://pbs.twimg.com/profile_images/542675764026429440/gPXHFroZ.png",addonString(30903).encode('utf-8'),'1',0,"https://s-media-cache-ak0.pinimg.com/originals/3f/be/f1/3fbef1cae14dea30c181f1f008839a1d.jpg")
	
	'''Pronovias'''
	list = []
	list.append('&youtube_ch=PronoviasTV')
	list.append('&youtube_id=zGczrEQytDY') #2017
	list.append('&youtube_id=rW14fQBpu5k') #2016
	list.append('&youtube_id=strsVGVi5OM') #2015
	list.append('&youtube_id=XfsXd3nlWyo') #2014
	addDir(addonString(30904).encode('utf-8'),list,17,"http://www.elopeinparis.com/wp-content/uploads/2014/05/pronovias-team-2015.jpg",addonString(30905).encode('utf-8'),'1',0,"http://www.elopeinparis.com/wp-content/uploads/2014/05/pronovias-team-2015.jpg")
	
	'''Elisabetta Franchi'''
	list = []
	list.append('&youtube_ch=ELISABETTAFRANCHI')
	list.append('&youtube_id=96SVkZhSOoE') #2017
	list.append('&youtube_id=hgqA-JHUNWs') #2016
	list.append('&youtube_id=u3bqUZua49s') #2015
	addDir(addonString(30906).encode('utf-8'),list,17,"http://www.wikifame.org/thumb.php?src=/photos/fb/37140.jpg",addonString(30907).encode('utf-8'),'1',0,"https://pmcwwd.files.wordpress.com/2016/09/elisabetta-franchi-spring-2017-collection-milan-fashion-week-mfw-ss17-068.jpg")
	
	
	CATEGORIES114A(name, iconimage, desc, fanart) #דף הבא

	
def CATEGORIES118(name, iconimage, desc, fanart):
	'''------------------------------
	---Classical-Music---------------
	------------------------------'''
	background = 118
	commonsearch = 'commonsearch118'
	
	CATEGORIES_RANDOM(background,fanart)
	CATEGORIES118Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
	'''Antonin Dvorak'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL72D45674D7B615C8')
	list.append('&youtube_pl=PLeCgNh_ukabqIPBiUWFJvdTNlegbB6n1D')
	list.append('&youtube_id=ETNoPqYAIPI')
	list.append('&youtube_id=3nSEMJW7UqE')
	list.append('&youtube_id=aPxHEN9lXCU')
	addDir(addonString(30707).encode('utf-8'),list,17,"https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Dvorak.jpg/220px-Dvorak.jpg",addonString(30708).encode('utf-8'),'1',0,"https://ichef.bbci.co.uk/images/ic/1920x1080/p01yqb0g.jpg")
	
	'''Antonio Vivaldi'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLkNcGVP98zKc3fgz1-JBt656r-WNTy-1r')
	list.append('&youtube_pl=PLC3124F2740F834CB')
	list.append('&youtube_id=nGdFHJXciAQ')
	list.append('&youtube_id=O6NRLYUThrY')
	list.append('&youtube_id=E2uOGOqIyC4')
	addDir(addonString(30711).encode('utf-8'),list,17,"http://iw.hdclassicalmusic.com/data/305/305_radiothumbnail.jpg",addonString(30712).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/ydbXpcgGVJQ/maxresdefault.jpg")
	
	'''Ennio Morricone'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL7UdecmcTxrgJvMSDvhDzE3MJZRJt1LgC')
	list.append('&youtube_id=Jjq6e1LJHxw')
	list.append('&youtube_id=VB6zwND6D5k')
	list.append('&youtube_id=LhOB8-cevIc')
	addDir(addonString(30709).encode('utf-8'),list,17,"https://upload.wikimedia.org/wikipedia/commons/a/a3/Ennio_Morricone_Cannes_2012.jpg",addonString(30710).encode('utf-8'),'1',0,"https://images6.alphacoders.com/309/309548.jpg")
	
	'''Luciano Pavarotti'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLWUeIS2Ft9tEmxiAyT8LGT6B_8YcEv7Pu')
	list.append('&youtube_id=jwhP4vZAh18')
	list.append('&youtube_id=2eVQ-RsXp3Y')
	list.append('&youtube_id=ITvDRP4Dm30')
	addDir(addonString(30705).encode('utf-8'),list,17,"http://static.universal-music.de/asset_new/279645/60/view/Luciano-Pavarotti.jpg",addonString(30706).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/aMZsx4O7P4A/maxresdefault.jpg")
	
	'''Ludwig van Beethoven'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL_xXZCm82ZklJlxjcZjS87kf8tdf2_0SW')
	list.append('&youtube_id=8ptfyhBjXj8')
	list.append('&youtube_id=4Tr0otuiQuU')
	list.append('&youtube_id=NVn1sJ5FjaU')
	addDir(addonString(30703).encode('utf-8'),list,17,"https://upload.wikimedia.org/wikipedia/commons/9/96/Beethoven_wiki.jpg",addonString(30704).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/8oqRV3tBTvk/maxresdefault.jpg")
	
	'''Wolfgang Mozart'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL_xjLdM_2tvKnPIN37-8whCoOy_n1oZQ7')
	list.append('&youtube_id=Rb0UmrCXxVA')
	list.append('&youtube_id=JTc1mDieQI8')
	addDir(addonString(30701).encode('utf-8'),list,17,"https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Wolfgang-amadeus-mozart_1.jpg/200px-Wolfgang-amadeus-mozart_1.jpg",addonString(30702).encode('utf-8'),'1',0,"https://i.ytimg.com/vi/-ir9hSJWYJ4/maxresdefault.jpg")
	
	CATEGORIES118A(name, iconimage, desc, fanart) #דף הבא
	
def CATEGORIES119(name, iconimage, desc, fanart):
	'''------------------------------
	---Radio-------------------------
	------------------------------'''
	background = 119
	addon = 'plugin.audio.jango'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Jango','plugin://'+addon,8,thumb,plot,addon,0,getAddonFanart(background, custom=fanart))
	
	addon = 'plugin.audio.99fm-playlists'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('99 FM','plugin://'+addon,8,thumb,plot,addon,0,getAddonFanart(background, custom=fanart))

	addon = 'plugin.audio.8tracks'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('8tracks','plugin://'+addon,8,thumb,plot,addon,0,getAddonFanart(background, custom=fanart))