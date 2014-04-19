# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AbyssRank(models.Model):
    player_id = models.IntegerField(primary_key=True)
    daily_ap = models.IntegerField()
    weekly_ap = models.IntegerField()
    ap = models.IntegerField()
    rank = models.IntegerField()
    top_ranking = models.IntegerField()
    old_ranking = models.IntegerField()
    daily_kill = models.IntegerField()
    weekly_kill = models.IntegerField()
    all_kill = models.IntegerField()
    max_rank = models.IntegerField()
    last_kill = models.IntegerField()
    last_ap = models.IntegerField()
    last_update = models.DecimalField(max_digits=20, decimal_places=0)
    class Meta:
        managed = False
        db_table = 'abyss_rank'

class AccountData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=65)
    activated = models.IntegerField()
    access_level = models.IntegerField()
    membership = models.IntegerField()
    last_server = models.IntegerField()
    last_ip = models.CharField(max_length=20, blank=True)
    last_mac = models.CharField(max_length=20, blank=True)
    ip_force = models.CharField(max_length=20, blank=True)
    credits = models.BigIntegerField()
    email = models.CharField(max_length=30, blank=True)
    last_logout = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'account_data'

class AccountTime(models.Model):
    account_id = models.IntegerField(primary_key=True)
    last_active = models.DateTimeField()
    expiration_time = models.DateTimeField(blank=True, null=True)
    session_duration = models.IntegerField(blank=True, null=True)
    accumulated_online = models.IntegerField(blank=True, null=True)
    accumulated_rest = models.IntegerField(blank=True, null=True)
    penalty_end = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'account_time'

class AionshopCategories(models.Model):
    categoryid = models.IntegerField(db_column='categoryId', primary_key=True) # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=255) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'aionshop_categories'

class AionshopItems(models.Model):
    itemuniqueid = models.BigIntegerField(db_column='itemUniqueId', primary_key=True) # Field name made lowercase.
    itemtemplateid = models.BigIntegerField(db_column='itemTemplateId') # Field name made lowercase.
    itemcount = models.IntegerField(db_column='itemCount') # Field name made lowercase.
    itemcategory = models.ForeignKey(AionshopCategories, db_column='itemCategory') # Field name made lowercase.
    itemprice = models.IntegerField(db_column='itemPrice') # Field name made lowercase.
    itemname = models.CharField(db_column='itemName', max_length=255) # Field name made lowercase.
    itemdesc = models.CharField(db_column='itemDesc', max_length=512) # Field name made lowercase.
    itemeyecatch = models.IntegerField(db_column='itemEyecatch') # Field name made lowercase.
    itemclassrestrict = models.CharField(db_column='itemClassRestrict', max_length=255, blank=True) # Field name made lowercase.
    itemserverrestrict = models.CharField(db_column='itemServerRestrict', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'aionshop_items'

class AionshopTransactions(models.Model):
    transaction_id = models.BigIntegerField(primary_key=True)
    server_id = models.IntegerField()
    item_unique_id = models.IntegerField()
    buy_timestamp = models.BigIntegerField()
    player_id = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'aionshop_transactions'

class Announcements(models.Model):
    id = models.IntegerField(primary_key=True)
    announce = models.TextField()
    faction = models.CharField(max_length=9)
    type = models.CharField(max_length=8)
    delay = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'announcements'

class ArenaTeams(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    points = models.IntegerField()
    name = models.CharField(unique=True, max_length=150)
    players = models.TextField()
    class Meta:
        managed = False
        db_table = 'arena_teams'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class BannedIp(models.Model):
    id = models.IntegerField(primary_key=True)
    mask = models.CharField(unique=True, max_length=45)
    time_end = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'banned_ip'

class BannedMac(models.Model):
    uniid = models.IntegerField(db_column='uniId', primary_key=True) # Field name made lowercase.
    address = models.CharField(max_length=20)
    playerid = models.IntegerField(db_column='playerId') # Field name made lowercase.
    time = models.DateTimeField()
    details = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'banned_mac'

class Blocks(models.Model):
    player = models.IntegerField()
    blocked_player = models.IntegerField()
    reason = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'blocks'

class Bookmark(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    char_id = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    world_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'bookmark'

class Broker(models.Model):
    id = models.IntegerField(primary_key=True)
    itempointer = models.IntegerField(db_column='itemPointer') # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId') # Field name made lowercase.
    itemcount = models.BigIntegerField(db_column='itemCount') # Field name made lowercase.
    seller = models.CharField(max_length=16)
    price = models.BigIntegerField()
    brokerrace = models.CharField(db_column='brokerRace', max_length=8) # Field name made lowercase.
    expiretime = models.DateTimeField(db_column='expireTime') # Field name made lowercase.
    settletime = models.DateTimeField(db_column='settleTime') # Field name made lowercase.
    sellerid = models.IntegerField(db_column='sellerId') # Field name made lowercase.
    issold = models.IntegerField(db_column='isSold') # Field name made lowercase.
    issettled = models.IntegerField(db_column='isSettled') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'broker'

class CaptchaCaptchastore(models.Model):
    id = models.IntegerField(primary_key=True)
    challenge = models.CharField(max_length=32)
    response = models.CharField(max_length=32)
    hashkey = models.CharField(unique=True, max_length=40)
    expiration = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'captcha_captchastore'

class CustomDroplist(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True) # Field name made lowercase.
    mobid = models.IntegerField(db_column='mobId') # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId') # Field name made lowercase.
    min = models.IntegerField()
    max = models.IntegerField()
    chance = models.FloatField()
    class Meta:
        managed = False
        db_table = 'custom_droplist'

class CustomSpawnGroups(models.Model):
    admin_id = models.IntegerField()
    group_name = models.CharField(max_length=255)
    spawned = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'custom_spawn_groups'

class CustomSpawns(models.Model):
    spawn_id = models.IntegerField(primary_key=True)
    object_id = models.IntegerField()
    admin_id = models.IntegerField()
    group_name = models.CharField(max_length=255, blank=True)
    npc_id = models.IntegerField()
    respawn = models.IntegerField()
    map_id = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    h = models.IntegerField()
    spawned = models.IntegerField()
    staticid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'custom_spawns'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class Friends(models.Model):
    player = models.IntegerField()
    friend = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'friends'

class Gameservers(models.Model):
    id = models.IntegerField(primary_key=True)
    mask = models.CharField(max_length=45)
    password = models.CharField(max_length=65)
    status = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'gameservers'

class Guilds(models.Model):
    player_id = models.IntegerField(primary_key=True)
    guild_id = models.IntegerField()
    last_quest = models.IntegerField()
    complete_time = models.DateTimeField(blank=True, null=True)
    current_quest = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'guilds'

class Inventory(models.Model):
    itemuniqueid = models.IntegerField(db_column='itemUniqueId', primary_key=True) # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId') # Field name made lowercase.
    itemcount = models.BigIntegerField(db_column='itemCount') # Field name made lowercase.
    itemcolor = models.IntegerField(db_column='itemColor') # Field name made lowercase.
    itemowner = models.IntegerField(db_column='itemOwner') # Field name made lowercase.
    itemcreator = models.CharField(db_column='itemCreator', max_length=50) # Field name made lowercase.
    itemcreationtime = models.DateTimeField(db_column='itemCreationTime') # Field name made lowercase.
    itemexisttime = models.BigIntegerField(db_column='itemExistTime') # Field name made lowercase.
    itemtradetime = models.IntegerField(db_column='itemTradeTime') # Field name made lowercase.
    isequiped = models.IntegerField(db_column='isEquiped') # Field name made lowercase.
    issoulbound = models.IntegerField(db_column='isSoulBound') # Field name made lowercase.
    slot = models.IntegerField()
    itemlocation = models.IntegerField(db_column='itemLocation', blank=True, null=True) # Field name made lowercase.
    enchant = models.IntegerField(blank=True, null=True)
    itemskin = models.IntegerField(db_column='itemSkin') # Field name made lowercase.
    fusioneditem = models.IntegerField(db_column='fusionedItem') # Field name made lowercase.
    optionalsocket = models.IntegerField(db_column='optionalSocket') # Field name made lowercase.
    optionalfusionsocket = models.IntegerField(db_column='optionalFusionSocket') # Field name made lowercase.
    charge = models.IntegerField()
    sealstats = models.IntegerField(db_column='sealStats') # Field name made lowercase.
    sealendtime = models.BigIntegerField(db_column='sealEndTime') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'inventory'

class ItemCooldowns(models.Model):
    player_id = models.IntegerField()
    delay_id = models.IntegerField()
    use_delay = models.IntegerField()
    reuse_time = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'item_cooldowns'

class ItemStones(models.Model):
    itemuniqueid = models.IntegerField(db_column='itemUniqueId') # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId') # Field name made lowercase.
    slot = models.IntegerField()
    category = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'item_stones'

class LegionAnnouncementList(models.Model):
    legion_id = models.IntegerField()
    announcement = models.CharField(max_length=255)
    date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'legion_announcement_list'

class LegionEmblems(models.Model):
    legion_id = models.IntegerField(primary_key=True)
    emblem_ver = models.IntegerField()
    color_r = models.IntegerField()
    color_g = models.IntegerField()
    color_b = models.IntegerField()
    custom = models.IntegerField()
    emblem_data = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'legion_emblems'

class LegionHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    legion_id = models.IntegerField()
    date = models.DateTimeField()
    history_type = models.CharField(max_length=15)
    name = models.CharField(max_length=16)
    class Meta:
        managed = False
        db_table = 'legion_history'

class LegionKinah(models.Model):
    legion_id = models.IntegerField(primary_key=True)
    count = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'legion_kinah'

class LegionMembers(models.Model):
    legion_id = models.IntegerField()
    player_id = models.IntegerField()
    nickname = models.CharField(max_length=16)
    rank = models.CharField(max_length=15)
    selfintro = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'legion_members'

class LegionWarehouseHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    legion_id = models.IntegerField()
    date = models.DateTimeField()
    history_type = models.CharField(max_length=19)
    name = models.CharField(max_length=16)
    item = models.CharField(max_length=25)
    class Meta:
        managed = False
        db_table = 'legion_warehouse_history'

class Legions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=16)
    rank = models.IntegerField()
    oldrank = models.IntegerField()
    level = models.IntegerField()
    contribution_points = models.IntegerField()
    deputy_permission1 = models.IntegerField()
    deputy_permission2 = models.IntegerField()
    legionary_permission1 = models.IntegerField()
    legionary_permission2 = models.IntegerField()
    centurion_permission1 = models.IntegerField()
    centurion_permission2 = models.IntegerField()
    volunteer_permission1 = models.IntegerField()
    volunteer_permission2 = models.IntegerField()
    disband_time = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'legions'

class Mail(models.Model):
    mailuniqueid = models.IntegerField(db_column='mailUniqueId', primary_key=True) # Field name made lowercase.
    mailrecipientid = models.IntegerField(db_column='mailRecipientId') # Field name made lowercase.
    sendername = models.CharField(db_column='senderName', max_length=35) # Field name made lowercase.
    mailtitle = models.CharField(db_column='mailTitle', max_length=20) # Field name made lowercase.
    mailmessage = models.CharField(db_column='mailMessage', max_length=1000) # Field name made lowercase.
    unread = models.IntegerField()
    attacheditemid = models.IntegerField(db_column='attachedItemId') # Field name made lowercase.
    attachedkinahcount = models.BigIntegerField(db_column='attachedKinahCount') # Field name made lowercase.
    express = models.IntegerField()
    recievedtime = models.DateTimeField(db_column='recievedTime') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mail'

class NpcShouts(models.Model):
    message_id = models.IntegerField()
    npc_id = models.IntegerField()
    event = models.CharField(max_length=11)
    param = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'npc_shouts'

class Petitions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    playerid = models.IntegerField(db_column='playerId') # Field name made lowercase.
    type = models.IntegerField()
    title = models.CharField(max_length=255)
    message = models.TextField()
    adddata = models.CharField(db_column='addData', max_length=255, blank=True) # Field name made lowercase.
    time = models.BigIntegerField()
    status = models.CharField(max_length=11)
    class Meta:
        managed = False
        db_table = 'petitions'

class PlayerAppearance(models.Model):
    player_id = models.IntegerField(primary_key=True)
    voice = models.IntegerField()
    skin_rgb = models.IntegerField()
    hair_rgb = models.IntegerField()
    lip_rgb = models.IntegerField()
    eye_rgb = models.IntegerField()
    face = models.IntegerField()
    hair = models.IntegerField()
    decoration = models.IntegerField()
    tattoo = models.IntegerField()
    face_contour = models.IntegerField()
    expression = models.IntegerField()
    jaw_line = models.IntegerField()
    forehead = models.IntegerField()
    eye_height = models.IntegerField()
    eye_space = models.IntegerField()
    eye_width = models.IntegerField()
    eye_size = models.IntegerField()
    eye_shape = models.IntegerField()
    eye_angle = models.IntegerField()
    brow_height = models.IntegerField()
    brow_angle = models.IntegerField()
    brow_shape = models.IntegerField()
    nose = models.IntegerField()
    nose_bridge = models.IntegerField()
    nose_width = models.IntegerField()
    nose_tip = models.IntegerField()
    cheeks = models.IntegerField()
    lip_height = models.IntegerField()
    mouth_size = models.IntegerField()
    lip_size = models.IntegerField()
    smile = models.IntegerField()
    lip_shape = models.IntegerField()
    chin_height = models.IntegerField()
    cheek_bones = models.IntegerField()
    ear_shape = models.IntegerField()
    head_size = models.IntegerField()
    neck = models.IntegerField()
    neck_length = models.IntegerField()
    shoulder_size = models.IntegerField()
    torso = models.IntegerField()
    chest = models.IntegerField()
    waist = models.IntegerField()
    hips = models.IntegerField()
    arm_thickness = models.IntegerField()
    hand_size = models.IntegerField()
    leg_thickness = models.IntegerField()
    foot_size = models.IntegerField()
    facial_ratio = models.IntegerField()
    face_shape = models.IntegerField()
    arm_length = models.IntegerField()
    leg_length = models.IntegerField()
    shoulders = models.IntegerField()
    height = models.FloatField()
    class Meta:
        managed = False
        db_table = 'player_appearance'

class PlayerEffects(models.Model):
    player_id = models.IntegerField()
    skill_id = models.IntegerField()
    delay_id = models.IntegerField()
    skill_lvl = models.IntegerField()
    current_time = models.IntegerField()
    reuse_delay = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'player_effects'

class PlayerEmotions(models.Model):
    player_id = models.IntegerField()
    emotion_id = models.IntegerField()
    emotion_expires_time = models.BigIntegerField()
    emotion_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'player_emotions'

class PlayerInstancecd(models.Model):
    playerid = models.IntegerField(db_column='playerId') # Field name made lowercase.
    instancemapid = models.IntegerField(db_column='instanceMapId') # Field name made lowercase.
    cdend = models.DateTimeField(db_column='CDEnd', blank=True, null=True) # Field name made lowercase.
    instanceid = models.IntegerField(db_column='instanceId') # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupId', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'player_instancecd'

class PlayerLifeStats(models.Model):
    player_id = models.IntegerField(primary_key=True)
    hp = models.IntegerField()
    mp = models.IntegerField()
    fp = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'player_life_stats'

class PlayerMacrosses(models.Model):
    player_id = models.IntegerField()
    order = models.IntegerField()
    macro = models.TextField()
    class Meta:
        managed = False
        db_table = 'player_macrosses'

class PlayerMotions(models.Model):
    player_id = models.IntegerField()
    motion_state = models.IntegerField()
    motion_active = models.IntegerField()
    motion_expires_time = models.BigIntegerField()
    motion_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'player_motions'

class PlayerPasskey(models.Model):
    account_id = models.IntegerField()
    passkey = models.CharField(max_length=8)
    class Meta:
        managed = False
        db_table = 'player_passkey'

class PlayerPets(models.Model):
    player_id = models.IntegerField()
    pet_id = models.IntegerField()
    decoration = models.IntegerField()
    name = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    feed_count = models.IntegerField()
    love_count = models.IntegerField()
    exp = models.IntegerField()
    feed_state = models.CharField(max_length=8)
    cd_started = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'player_pets'

class PlayerPunishments(models.Model):
    player_id = models.IntegerField(primary_key=True)
    punishment_status = models.IntegerField(blank=True, null=True)
    punishment_timer = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'player_punishments'

class PlayerQuests(models.Model):
    player_id = models.IntegerField()
    quest_id = models.IntegerField()
    status = models.CharField(max_length=10)
    quest_vars = models.IntegerField()
    complete_count = models.IntegerField()
    complete_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'player_quests'

class PlayerRecipes(models.Model):
    player_id = models.IntegerField()
    recipe_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'player_recipes'

class PlayerSettings(models.Model):
    player_id = models.IntegerField()
    settings_type = models.IntegerField()
    settings = models.TextField()
    class Meta:
        managed = False
        db_table = 'player_settings'

class PlayerSkills(models.Model):
    player_id = models.IntegerField()
    skillid = models.IntegerField(db_column='skillId') # Field name made lowercase.
    skilllevel = models.IntegerField(db_column='skillLevel') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'player_skills'

class PlayerTitles(models.Model):
    player_id = models.IntegerField()
    title_id = models.IntegerField()
    title_expires_time = models.BigIntegerField()
    title_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'player_titles'

class PlayerWorldBans(models.Model):
    player = models.IntegerField(primary_key=True)
    by = models.CharField(max_length=255)
    duration = models.BigIntegerField()
    date = models.BigIntegerField()
    reason = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'player_world_bans'

class Players(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    account_id = models.IntegerField()
    account_name = models.CharField(max_length=50)
    exp = models.BigIntegerField()
    recoverexp = models.BigIntegerField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    heading = models.IntegerField()
    world_id = models.IntegerField()
    gender = models.CharField(max_length=6)
    race = models.CharField(max_length=9)
    player_class = models.CharField(max_length=13)
    creation_date = models.DateTimeField()
    deletion_date = models.DateTimeField(blank=True, null=True)
    last_online = models.DateTimeField()
    cube_size = models.IntegerField()
    advanced_stigma_slot_size = models.IntegerField()
    warehouse_size = models.IntegerField()
    mailboxletters = models.IntegerField(db_column='mailboxLetters') # Field name made lowercase.
    brokerkinah = models.BigIntegerField(db_column='brokerKinah') # Field name made lowercase.
    bind_point = models.IntegerField()
    title_id = models.IntegerField()
    online = models.IntegerField()
    note = models.TextField(blank=True)
    repletionstate = models.BigIntegerField()
    bg_points = models.IntegerField()
    personal_rating = models.IntegerField()
    arena_points = models.IntegerField()
    partner_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'players'

class PurchaseLimit(models.Model):
    player_id = models.IntegerField()
    itemid = models.IntegerField(db_column='itemId') # Field name made lowercase.
    itemcount = models.BigIntegerField(db_column='itemCount') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'purchase_limit'

class ServerVariables(models.Model):
    key = models.CharField(primary_key=True, max_length=30)
    value = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'server_variables'

class SiegeLocations(models.Model):
    id = models.IntegerField(primary_key=True)
    race = models.CharField(max_length=9)
    legion_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'siege_locations'

class SiegeLog(models.Model):
    log_uuid = models.BigIntegerField(primary_key=True)
    legion_name = models.CharField(max_length=255)
    action = models.CharField(max_length=7)
    tstamp = models.BigIntegerField()
    siegeloc_id = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'siege_log'

class SkillMotions(models.Model):
    motion_name = models.CharField(max_length=255)
    skill_id = models.IntegerField()
    attack_speed = models.IntegerField()
    weapon_type = models.CharField(max_length=255)
    off_weapon_type = models.CharField(max_length=255)
    time = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'skill_motions'

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'south_migrationhistory'

class SpecialSpawns(models.Model):
    id = models.BigIntegerField(primary_key=True)
    stage = models.IntegerField()
    round = models.IntegerField()
    npc_id = models.IntegerField()
    world_id = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    h = models.IntegerField()
    flag = models.IntegerField()
    race = models.CharField(max_length=9)
    class Meta:
        managed = False
        db_table = 'special_spawns'

class Surveys(models.Model):
    survey_id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    title = models.CharField(max_length=80)
    message = models.CharField(max_length=1024)
    select_text = models.CharField(max_length=50)
    itemid = models.IntegerField(db_column='itemId') # Field name made lowercase.
    itemcount = models.BigIntegerField(db_column='itemCount') # Field name made lowercase.
    itemtradetime = models.IntegerField(db_column='itemTradeTime') # Field name made lowercase.
    itemexisttime = models.BigIntegerField(db_column='itemExistTime') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'surveys'

