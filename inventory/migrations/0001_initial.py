# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Inventory'
        db.create_table(u'inventory_inventory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('of_the_round_table', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'inventory', ['Inventory'])

        # Adding model 'Contact'
        db.create_table(u'inventory_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'inventory', ['Contact'])

        # Adding model 'Tag'
        db.create_table(u'inventory_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Contact'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'inventory', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Inventory'
        db.delete_table(u'inventory_inventory')

        # Deleting model 'Contact'
        db.delete_table(u'inventory_contact')

        # Deleting model 'Tag'
        db.delete_table(u'inventory_tag')


    models = {
        u'inventory.contact': {
            'Meta': {'object_name': 'Contact'},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'inventory.inventory': {
            'Meta': {'object_name': 'Inventory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'of_the_round_table': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'inventory.tag': {
            'Meta': {'object_name': 'Tag'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['inventory']