# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Input.raw_y'
        db.alter_column(u'mltest_input', 'raw_y', self.gf('django.db.models.fields.CharField')(max_length=10000))

        # Changing field 'Input.raw_x'
        db.alter_column(u'mltest_input', 'raw_x', self.gf('django.db.models.fields.CharField')(max_length=10000))

    def backwards(self, orm):

        # Changing field 'Input.raw_y'
        db.alter_column(u'mltest_input', 'raw_y', self.gf('django.db.models.fields.CharField')(max_length=1000))

        # Changing field 'Input.raw_x'
        db.alter_column(u'mltest_input', 'raw_x', self.gf('django.db.models.fields.CharField')(max_length=1000))

    models = {
        u'mltest.input': {
            'Meta': {'object_name': 'Input'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'raw_x': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'raw_y': ('django.db.models.fields.CharField', [], {'max_length': '10000'})
        }
    }

    complete_apps = ['mltest']