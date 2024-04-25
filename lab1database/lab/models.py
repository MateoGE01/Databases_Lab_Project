from django.db import models



class Database(models.Model):
    id = models.IntegerField(primary_key=True)
    course_id = models.CharField(max_length=255, blank=True, null=True)    
    userid_di = models.CharField(max_length=255, blank=True, null=True)    
    registered = models.IntegerField(blank=True, null=True)
    viewed = models.IntegerField(blank=True, null=True)
    explored = models.IntegerField(blank=True, null=True)
    certified = models.IntegerField(blank=True, null=True)
    final_cc_cname_di = models.CharField(max_length=255, blank=True, null=True)
    loe_di = models.CharField(max_length=255, blank=True, null=True)       
    yob = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=5, blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)
    start_time_di = models.DateField(blank=True, null=True)
    last_event_di = models.DateField(blank=True, null=True)
    nevents = models.IntegerField(blank=True, null=True)
    ndays_act = models.IntegerField(blank=True, null=True)
    nplay_video = models.IntegerField(blank=True, null=True)
    nchapters = models.IntegerField(blank=True, null=True)
    nforum_posts = models.IntegerField(blank=True, null=True)
    incomplete_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses_clean_tabla'

    def __str__(self):
        return str(self.id)