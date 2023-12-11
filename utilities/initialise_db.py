import mysql.connector
import sys


def Connect():
    conn=None
    try:
        conn=mysql.connector.Connect(
            host='sql12.freesqldatabase.com',
            username='sql12669532',
            password='wlIArNGzxs',
            database='sql12669532'
        )


    except:
        print('Error', sys.exc_info())

    finally:
        return conn
    




def create_db():
    conn=None

    #creation
    #sql0="""DROP DATABASE IF EXISTS futelibs"""
    #sql1="""CREATE DATABASE futelibs"""
    sql2="""USE sql12669532"""
    sql3="""create table admin(aid int primary key,name varchar(50),doj date,email varchar(50),pass varchar(20))"""
    sql4="""create table employee(eid int primary key,name varchar(50),doj date,email varchar(50),pass varchar(20))"""
    sql5="""create table members(mid int primary key,name varchar(50),doj date,email varchar(50),pass varchar(20))"""
    sql6="""create table book(bid int primary key,name varchar(50),author varchar(50),holder int)"""
    sql7="""create table raw_tr(tid int primary key,mid int,bid int,eid int,issue_date date,status varchar(10),re_date date,fine_paid int)"""

    '''
        create view tran_v as(select tid,mid,bid,eid,issue_date,status,
        DATE_ADD(issue_date,interval 10 day) as exp_re_date,
        IF(status='pending',
        IF(DATEDIFF(DATE_ADD(issue_date,interval 10 day),CURDATE())<0,'delayed',DATEDIFF(DATE_ADD(issue_date,interval 10 day),CURDATE())),
        'returned') as days_left,
        IF(status='pending',
        IF(DATEDIFF(DATE_ADD(issue_date,interval 10 day),CURDATE())<0,(-1)*DATEDIFF(DATE_ADD(issue_date,interval 10 day),CURDATE()),0),
        IF(re_date>DATE_ADD(issue_date,interval 10 day),(-1)*DATEDIFF(DATE_ADD(issue_date,interval 10 day),re_date),0))  as delay,
        IF(DATEDIFF(DATE_ADD(issue_date,interval 10 day),CURDATE())<0 and status='pending',(-10)*DATEDIFF(DATE_ADD(issue_date,interval 10 day),CURDATE()),0) as fine_payable,
        fine_paid,re_date from raw_tr)
    '''
    sql8="""create view tran_v as(select tid,mid,bid,eid,issue_date,status,DATE_ADD(issue_date,interval 10 day) as exp_re_date,IF(status='pending',IF(DATEDIFF(DATE_ADD(issue_date,interval 10 day),CURDATE())<0,'delayed',DATEDIFF(DATE_ADD(issue_date,interval 10 day),CURDATE())),'returned') as days_left,IF(status='pending',IF(DATEDIFF(DATE_ADD(issue_date,interval 10 day),CURDATE())<0,(-1)*DATEDIFF(DATE_ADD(issue_date,interval 10 day),CURDATE()),0),IF(re_date>DATE_ADD(issue_date,interval 10 day),(-1)*DATEDIFF(DATE_ADD(issue_date,interval 10 day),re_date),0))  as delay,IF(DATEDIFF(DATE_ADD(issue_date,interval 10 day),CURDATE())<0 and status='pending',(-10)*DATEDIFF(DATE_ADD(issue_date,interval 10 day),CURDATE()),0) as fine_payable,fine_paid,re_date from raw_tr)"""
    sql9= """create view pending_v as(select tran_v.mid as mid,tran_v.tid,tran_v.issue_date,book.name,tran_v.days_left,tran_v.delay,tran_v.fine_payable from tran_v,book where book.bid=tran_v.bid and status='pending')"""
    sql10 ="""create view returned_v as(select tran_v.mid as mid,tran_v.tid,tran_v.issue_date,book.name,tran_v.re_date,tran_v.delay,tran_v.fine_paid from tran_v,book where book.bid=tran_v.bid and status='returned')"""
    sql11="""create view maxi as(select max(admin.aid) as aid,max(members.mid) as mid,max(employee.eid) as eid,max(raw_tr.tid) as tid,max(book.bid) as bid from admin,employee,members,raw_tr,book)"""
    
    #insertion
    sql12="""insert into members values(130,'Shyu',curdate() ,'shyu.kun@outlook.com','wingardium@laviosar')"""
    sql13="""insert into employee values(102,'Nao',curdate(),'nao.chan@outlook.com','minions@si#')"""
    sql14="""insert into admin values(101,'ALAM',curdate(),'sufiuwu@outlook.com','banana@nana#')"""
    sql15="""insert into book values(111,'Alice in Wonderland','Lewis Carrol',130),(112,'Harry Potter and the Philosopher''s Stone',' J. K. Rowling',0),(113,'Harry Potter and the Chamber of Secrets',' J. K. Rowling',0),(114,'Harry Potter and the Prisoner of Azkaban',' J. K. Rowling',0),(115,'Harry Potter and the Goblet of Fire',' J. K. Rowling',0),(116,'Harry Potter and the Order of the Phoenix',' J. K. Rowling',0),(117,'Harry Potter and the Half-Blood Prince',' J. K. Rowling',0),(118,'Harry Potter and the Deathly Hallows',' J. K. Rowling',0),(119,'The Adventures of Tom Sawyer','Mark Twain',0),(120,'Gulliver’s Travels','Jonathan Swift',130),(121,'Robinson Crusoe','Daniel Defoe',0),(122,'Around the World in Eighty Days','Jules Verne',0),(123,'Moby Dick','Herman Melville',0),(124,'David Copperfield','Charles Dickens',0)"""
    sql16="""insert into raw_tr values(1, 130, 111, 102, '20230926', 'returned', '20231010', 40),(2, 130, 117, 102, '20231005', 'returned', '20231006', 0),(3, 130, 121, 102, '20230930', 'returned', '20231022', 120),(4, 130, 123, 102, '20231010', 'returned', '20231024', 40),(5, 130, 120, 102, '20231021','pending', NULL, NULL),(6, 130, 111, 102, '20231024','pending', NULL, NULL)"""


    try:
        conn=Connect()
        cursor=conn.cursor()


        #cursor.execute(sql0)
        #cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        cursor.execute(sql4)
        cursor.execute(sql5)
        cursor.execute(sql6)
        cursor.execute(sql7)
        cursor.execute(sql8)
        cursor.execute(sql9)
        cursor.execute(sql10)
        cursor.execute(sql11)
        cursor.execute(sql12)
        cursor.execute(sql13)
        cursor.execute(sql14)
        cursor.execute(sql15)
        cursor.execute(sql16)
        
        conn.commit()
        cursor.close()
        conn.close()

    except:
        print('Error',sys.exc_info())
        print('DATABASE INITIALISATION  FAILED')

    finally:
        del conn,sql2,sql3,sql4,sql5,sql6,sql7,sql8,sql9,sql10,sql11,sql12,sql13,sql14,sql15,sql16



