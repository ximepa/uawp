from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import hashlib
import base64

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


class AccountData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=65)
    activated = models.IntegerField(blank=True, null=True)
    access_level = models.IntegerField(blank=True, null=True)
    membership = models.IntegerField(blank=True, null=True)
    last_server = models.IntegerField(blank=True, null=True)
    last_ip = models.CharField(max_length=20, blank=True)
    last_mac = models.CharField(max_length=20, blank=True)
    ip_force = models.CharField(max_length=20, blank=True)
    credits = models.BigIntegerField()
    email = models.CharField(max_length=30, blank=True)
    last_logout = models.BigIntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def check_password(self, raw_password):
        encoded_password = base64.b64encode(hashlib.sha1(raw_password).hexdigest().decode('hex'))
        return self.password == encoded_password

    class Meta:
        managed = False
        db_table = 'account_data'


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    game_acc = models.ManyToManyField('AccountData', related_name='game_accounts', blank=True)
    coints = models.IntegerField(default=0)
    is_premium = models.BooleanField(default=False,)
    is_vip = models.BooleanField(default=False,)
    premium_start = models.DateTimeField(null=True, blank=True)
    premium_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
          return "%s's profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

User.profile = property(lambda u: u.get_profile() )

