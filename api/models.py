# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class JndUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    agent_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=20)
    user_nickname = models.CharField(max_length=30)
    user_tel = models.CharField(max_length=11)
    user_psw = models.CharField(max_length=255, blank=True, null=True)
    user_wx_openid = models.CharField(max_length=40, blank=True, null=True)
    user_create_time = models.IntegerField()
    user_lasttime = models.IntegerField()
    user_ip = models.CharField(max_length=25)
    user_credit = models.IntegerField()
    user_login_num = models.SmallIntegerField()
    user_yesno = models.IntegerField()
    user_balance = models.DecimalField(max_digits=18, decimal_places=2)
    belong_to_role = models.SmallIntegerField()
    user_midou = models.PositiveIntegerField()
    user_gold = models.DecimalField(max_digits=18, decimal_places=2)
    user_realname = models.CharField(max_length=20)
    user_headimg = models.CharField(max_length=201)
    user_motto = models.CharField(max_length=80)
    user_wx_unionid = models.CharField(max_length=50)
    user_wx_openid_gj = models.CharField(max_length=40)
    user_wx_openid_sj = models.CharField(max_length=40)
    user_sex = models.IntegerField()
    user_pay_psw = models.CharField(max_length=200)
    user_gold_lock = models.IntegerField()
    user_balance_lock = models.IntegerField()
    user_credit_lock = models.IntegerField()
    grade_id = models.SmallIntegerField()
    user_midou_lock_num = models.BigIntegerField()
    user_gold_lock_num = models.DecimalField(max_digits=18, decimal_places=2)
    user_balance_lock_num = models.DecimalField(max_digits=18, decimal_places=2)
    id_card_no = models.CharField(max_length=20)
    user_source = models.IntegerField(blank=True, null=True)
    vip_expires_time = models.PositiveIntegerField()
    vip_free_collection_count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jnd_user'


class JndUserInvitation(models.Model):
    user_id = models.PositiveIntegerField()
    top_user_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jnd_user_invitation'


class JndUserMidou(models.Model):
    user_id = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    data_id = models.CharField(max_length=20)
    table_id = models.CharField(max_length=20)
    num = models.DecimalField(max_digits=18, decimal_places=2)
    num_before = models.DecimalField(max_digits=18, decimal_places=2)
    num_after = models.DecimalField(max_digits=18, decimal_places=2)
    remark = models.CharField(max_length=30)
    create_time = models.PositiveIntegerField()
    type_id = models.PositiveIntegerField()
    user_identity_id = models.PositiveIntegerField()
    from_type = models.PositiveIntegerField()
    agent_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jnd_user_midou'
