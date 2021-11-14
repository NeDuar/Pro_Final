from django.db import models
import psycopg2
# Create your models here.


class Tables(models.Model):
    conn = psycopg2.connect("dbname='TiendaProyectoFinal' user='postgres' host='localhost' password='201903916-Proyecto' port='5433'")
    cur = conn.cursor()
    # """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'"""
    cur.execute("SELECT \"username\", \"ip_address\", \"id\", \"attempt_time\" FROM \"axes_accesslog\";")
    rows = cur.fetchall()


class Tables2(models.Model):
    conn = psycopg2.connect("dbname='TiendaProyectoFinal' user='postgres' host='localhost' password='201903916-Proyecto' port='5433'")
    cur = conn.cursor()
    # """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'"""
    cur.execute("SELECT \"username\", \"ip_address\", \"id\", \"attempt_time\", \"failures_since_start\" FROM \"axes_accessattempt\";")
    rows = cur.fetchall()


class Tables3(models.Model):
    conn = psycopg2.connect("dbname='TiendaProyectoFinal' user='postgres' host='localhost' password='201903916-Proyecto' port='5433'")
    cur = conn.cursor()
    # """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'"""
    cur.execute("SELECT \"id\", \"product_id\", \"quantity\", \"created_at\"  FROM \"orderlines\";")
    rows = cur.fetchall()


class Tables4(models.Model):
    conn = psycopg2.connect("dbname='TiendaProyectoFinal' user='postgres' host='localhost' password='201903916-Proyecto' port='5433'")
    cur = conn.cursor()
    # """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'"""
    cur.execute("SELECT \"id\", \"slug\", \"price\", \"stock\" FROM \"products\";")
    rows = cur.fetchall()