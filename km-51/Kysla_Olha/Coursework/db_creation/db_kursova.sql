/*==============================================================*/
/* DBMS name:      ORACLE Version 11g                           */
/* Created on:     04.11.2018 13:13:52                          */
/*==============================================================*/


alter table Makeups_features
   drop constraint FK_MAKEUPS_FEATURE_MAKEUPS;

alter table Makeups_features
   drop constraint FK_MAKEUPS_FEATURE_FEATURES;

alter table "User"
   drop constraint FK_USER_ROLES;

alter table User_feature
   drop constraint FK_USERS_FEATURE_FEATURES;

alter table User_feature
   drop constraint FK_USERS_FEATURES_USER;

drop table Feature cascade constraints;

drop table Makeup cascade constraints;

drop index makeups_have_features_FK;

drop index makeups_have_features2_FK;

drop table Makeups_features cascade constraints;

drop table Role cascade constraints;

drop index users_have_role_FK;

drop table "User" cascade constraints;

drop index users_have_features_FK;

drop index users_have_features2_FK;

drop table User_feature cascade constraints;

/*==============================================================*/
/* Table: Feature                                               */
/*==============================================================*/
create table Feature 
(
   feature_name         VARCHAR2(20)         not null,
   constraint PK_FEATURE primary key (feature_name)
);

/*==============================================================*/
/* Table: Makeup                                                */
/*==============================================================*/
create table Makeup 
(
   makeup_id            INTEGER              not null,
   makeup_name          VARCHAR2(30)         not null,
   makeup_price         INTEGER              not null,
   makeup_quantity      INTEGER              not null,
   makeup_description   CLOB,
   constraint PK_MAKEUP primary key (makeup_id)
);

/*==============================================================*/
/* Table: Makeups_features                                      */
/*==============================================================*/
create table Makeups_features 
(
   makeup_id_fk         INTEGER              not null,
   feature_name_fk      VARCHAR2(20)         not null,
   makeup_attribute     VARCHAR2(20)         not null,
   constraint PK_MAKEUPS_FEATURES primary key (makeup_id_fk, feature_name_fk)
);

/*==============================================================*/
/* Index: makeups_have_features2_FK                             */
/*==============================================================*/
create index makeups_have_features2_FK on Makeups_features (
   feature_name_fk ASC
);

/*==============================================================*/
/* Index: makeups_have_features_FK                              */
/*==============================================================*/
create index makeups_have_features_FK on Makeups_features (
   makeup_id_fk ASC
);

/*==============================================================*/
/* Table: Role                                                  */
/*==============================================================*/
create table Role 
(
   role                 VARCHAR2(15)         not null,
   constraint PK_ROLE primary key (role)
);

/*==============================================================*/
/* Table: "User"                                                */
/*==============================================================*/
create table "User" 
(
   role_fk              VARCHAR2(15)         not null,
   user_name            VARCHAR2(30)         not null,
   user_email           VARCHAR2(20)         not null,
   user_pass            VARCHAR2(20)         not null,
   constraint PK_USER primary key (user_email)
);

/*==============================================================*/
/* Index: users_have_role_FK                                    */
/*==============================================================*/
create index users_have_role_FK on "User" (
   role_fk ASC
);

/*==============================================================*/
/* Table: User_feature                                          */
/*==============================================================*/
create table User_feature 
(
   feature_name         VARCHAR2(20)         not null,
   user_email_fk        VARCHAR2(20)         not null,
   user_attribute       VARCHAR2(20)         not null,
   constraint PK_USER_FEATURE primary key (feature_name, user_email_fk)
);

/*==============================================================*/
/* Index: users_have_features2_FK                               */
/*==============================================================*/
create index users_have_features2_FK on User_feature (
   user_email_fk ASC
);

/*==============================================================*/
/* Index: users_have_features_FK                                */
/*==============================================================*/
create index users_have_features_FK on User_feature (
   feature_name ASC
);

alter table Makeups_features
   add constraint FK_MAKEUPS_FEATURE_MAKEUPS foreign key (makeup_id_fk)
      references Makeup (makeup_id);

alter table Makeups_features
   add constraint FK_MAKEUPS_FEATURE_FEATURES foreign key (feature_name_fk)
      references Feature (feature_name);

alter table "User"
   add constraint FK_USER_ROLES foreign key (role_fk)
      references Role (role);

alter table User_feature
   add constraint FK_USERS_FEATURE_FEATURES foreign key (feature_name)
      references Feature (feature_name);

alter table User_feature
   add constraint FK_USERS_FEATURES_USER foreign key (user_email_fk)
      references "User" (user_email);

