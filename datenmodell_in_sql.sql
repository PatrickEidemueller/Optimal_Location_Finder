/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     11/29/2021 3:53:02 PM                        */
/*==============================================================*/


drop index THIRD_FK;

drop index FIRST_FK;

drop index RELATIONSHIP_7_FK;

drop index BUSINESS_PK;

drop table BUSINESS;

drop index CATEGORIE_PK;

drop table CATEGORIE;

drop index CHECK_IN2_FK;

drop index CHECK_IN_FK;

drop index CHECK_IN_PK;

drop table CHECK_IN;

drop index HAS_CATEGORIE2_FK;

drop index HAS_CATEGORIE_FK;

drop index HAS_CATEGORIE_PK;

drop table HAS_CATEGORIE;

drop index IS_FRIEND2_FK;

drop index IS_FRIEND_FK;

drop index IS_FRIEND_PK;

drop table IS_FRIEND;

drop index WRITES_FK;

drop index HAS2_FK;

drop index REVIEW_PK;

drop table REVIEW;

drop index STATION_PK;

drop table STATION;

drop index USER_PK;

drop table "USER";

drop index RELATIONSHIP_5_FK;

drop index WEATHER_PK;

drop table WEATHER;

/*==============================================================*/
/* Table: BUSINESS                                              */
/*==============================================================*/
create table BUSINESS (
   IS_OPEN              INT4                 null,
   BUSINESS_ID          VARCHAR(22)          not null,
   ID                   VARCHAR(25)          not null,
   STA_ID               VARCHAR(25)          not null,
   STA_ID2              VARCHAR(25)          not null,
   NAME                 CHAR(25)             not null,
   ADDRESS              VARCHAR(25)          not null,
   CITY                 VARCHAR(25)          not null,
   STATE                VARCHAR(25)          not null,
   POSTAL               VARCHAR(25)          not null,
   LATITUDE             DECIMAL(8,6)         not null,
   LONGITUDE            DECIMAL(9,6)         not null,
   STARS                FLOAT8               null,
   REVIEW_COUNT         INT4                 null,
   DISTANCE_FIRST       DECIMAL              null,
   DISTANCE_SECOND      DECIMAL              null,
   DISTANCE_THIRD       DECIMAL              null,
   CATEGORIES           TEXT                 null,
   constraint PK_BUSINESS primary key (BUSINESS_ID)
);

/*==============================================================*/
/* Index: BUSINESS_PK                                           */
/*==============================================================*/
create unique index BUSINESS_PK on BUSINESS (
BUSINESS_ID
);

/*==============================================================*/
/* Index: RELATIONSHIP_7_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_7_FK on BUSINESS (
STA_ID2
);

/*==============================================================*/
/* Index: FIRST_FK                                              */
/*==============================================================*/
create  index FIRST_FK on BUSINESS (
STA_ID
);

/*==============================================================*/
/* Index: THIRD_FK                                              */
/*==============================================================*/
create  index THIRD_FK on BUSINESS (
ID
);

/*==============================================================*/
/* Table: CATEGORIE                                             */
/*==============================================================*/
create table CATEGORIE (
   CATEGORIES           TEXT                 null,
   CATEGORIE_ID         INT4                 not null,
   constraint PK_CATEGORIE primary key (CATEGORIE_ID)
);

/*==============================================================*/
/* Index: CATEGORIE_PK                                          */
/*==============================================================*/
create unique index CATEGORIE_PK on CATEGORIE (
CATEGORIE_ID
);

/*==============================================================*/
/* Table: CHECK_IN                                              */
/*==============================================================*/
create table CHECK_IN (
   USER_ID              VARCHAR(22)          not null,
   BUSINESS_ID          VARCHAR(22)          not null,
   constraint PK_CHECK_IN primary key (USER_ID, BUSINESS_ID)
);

/*==============================================================*/
/* Index: CHECK_IN_PK                                           */
/*==============================================================*/
create unique index CHECK_IN_PK on CHECK_IN (
USER_ID,
BUSINESS_ID
);

/*==============================================================*/
/* Index: CHECK_IN_FK                                           */
/*==============================================================*/
create  index CHECK_IN_FK on CHECK_IN (
USER_ID
);

/*==============================================================*/
/* Index: CHECK_IN2_FK                                          */
/*==============================================================*/
create  index CHECK_IN2_FK on CHECK_IN (
BUSINESS_ID
);

/*==============================================================*/
/* Table: HAS_CATEGORIE                                         */
/*==============================================================*/
create table HAS_CATEGORIE (
   CATEGORIE_ID         INT4                 not null,
   BUSINESS_ID          VARCHAR(22)          not null,
   constraint PK_HAS_CATEGORIE primary key (CATEGORIE_ID, BUSINESS_ID)
);

/*==============================================================*/
/* Index: HAS_CATEGORIE_PK                                      */
/*==============================================================*/
create unique index HAS_CATEGORIE_PK on HAS_CATEGORIE (
CATEGORIE_ID,
BUSINESS_ID
);

/*==============================================================*/
/* Index: HAS_CATEGORIE_FK                                      */
/*==============================================================*/
create  index HAS_CATEGORIE_FK on HAS_CATEGORIE (
CATEGORIE_ID
);

/*==============================================================*/
/* Index: HAS_CATEGORIE2_FK                                     */
/*==============================================================*/
create  index HAS_CATEGORIE2_FK on HAS_CATEGORIE (
BUSINESS_ID
);

/*==============================================================*/
/* Table: IS_FRIEND                                             */
/*==============================================================*/
create table IS_FRIEND (
   USER_ID              VARCHAR(22)          not null,
   USE_USER_ID          VARCHAR(22)          not null,
   constraint PK_IS_FRIEND primary key (USER_ID, USE_USER_ID)
);

/*==============================================================*/
/* Index: IS_FRIEND_PK                                          */
/*==============================================================*/
create unique index IS_FRIEND_PK on IS_FRIEND (
USER_ID,
USE_USER_ID
);

/*==============================================================*/
/* Index: IS_FRIEND_FK                                          */
/*==============================================================*/
create  index IS_FRIEND_FK on IS_FRIEND (
USER_ID
);

/*==============================================================*/
/* Index: IS_FRIEND2_FK                                         */
/*==============================================================*/
create  index IS_FRIEND2_FK on IS_FRIEND (
USE_USER_ID
);

/*==============================================================*/
/* Table: REVIEW                                                */
/*==============================================================*/
create table REVIEW (
   REVIEW_ID            VARCHAR(1024)        not null,
   BUSINESS_ID          VARCHAR(22)          not null,
   USER_ID              VARCHAR(22)          not null,
   STARS                FLOAT8               not null,
   DATE                 DATE                 null,
   TEXT                 TEXT                 not null,
   USEFUL               INT4                 null,
   FUNNY                INT4                 null,
   COOL                 INT4                 null,
   constraint PK_REVIEW primary key (REVIEW_ID)
);

/*==============================================================*/
/* Index: REVIEW_PK                                             */
/*==============================================================*/
create unique index REVIEW_PK on REVIEW (
REVIEW_ID
);

/*==============================================================*/
/* Index: HAS2_FK                                               */
/*==============================================================*/
create  index HAS2_FK on REVIEW (
BUSINESS_ID
);

/*==============================================================*/
/* Index: WRITES_FK                                             */
/*==============================================================*/
create  index WRITES_FK on REVIEW (
USER_ID
);

/*==============================================================*/
/* Table: STATION                                               */
/*==============================================================*/
create table STATION (
   ID                   VARCHAR(25)          not null,
   LATITUDE             DECIMAL(8,6)         null,
   LONGITUDE            DECIMAL(9,6)         null,
   ELEVATION            FLOAT8               null,
   STATE                VARCHAR(25)          null,
   NAME                 CHAR(25)             null,
   constraint PK_STATION primary key (ID)
);

/*==============================================================*/
/* Index: STATION_PK                                            */
/*==============================================================*/
create unique index STATION_PK on STATION (
ID
);

/*==============================================================*/
/* Table: "USER"                                                */
/*==============================================================*/
create table "USER" (
   USER_ID              VARCHAR(22)          not null,
   NAME                 CHAR(25)             not null,
   REVIEW_COUNT         INT4                 null,
   YELPING_SINCE        INT4                 null,
   AVERAGE_STARS        FLOAT8               null,
   USEFUL               INT4                 null,
   FANS                 INT4                 null,
   FUNNY                INT4                 null,
   COOL                 INT4                 null,
   constraint PK_USER primary key (USER_ID)
);

/*==============================================================*/
/* Index: USER_PK                                               */
/*==============================================================*/
create unique index USER_PK on "USER" (
USER_ID
);

/*==============================================================*/
/* Table: WEATHER                                               */
/*==============================================================*/
create table WEATHER (
   ID                   VARCHAR(25)          not null,
   DATE                 DATE                 not null,
   TMIN                 DECIMAL(8)           null,
   TMAX                 DECIMAL(8)           null,
   PRCP                 DECIMAL(8)           null,
   SNOW                 DECIMAL(8)           null,
   SNWD                 DECIMAL(8)           null,
   ACSC                 DECIMAL(8)           null,
   TAVG                 DECIMAL(8)           null,
   PSUN                 DECIMAL(8)           null,
   AWND                 DECIMAL(8)           null,
   constraint PK_WEATHER primary key (ID, DATE)
);

/*==============================================================*/
/* Index: WEATHER_PK                                            */
/*==============================================================*/
create unique index WEATHER_PK on WEATHER (
ID,
DATE
);

/*==============================================================*/
/* Index: RELATIONSHIP_5_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_5_FK on WEATHER (
ID
);

alter table BUSINESS
   add constraint FK_BUSINESS_FIRST_STATION foreign key (STA_ID)
      references STATION (ID)
      on delete restrict on update restrict;

alter table BUSINESS
   add constraint FK_BUSINESS_RELATIONS_STATION foreign key (STA_ID2)
      references STATION (ID)
      on delete restrict on update restrict;

alter table BUSINESS
   add constraint FK_BUSINESS_THIRD_STATION foreign key (ID)
      references STATION (ID)
      on delete restrict on update restrict;

alter table CHECK_IN
   add constraint FK_CHECK_IN_CHECK_IN_USER foreign key (USER_ID)
      references "USER" (USER_ID)
      on delete restrict on update restrict;

alter table CHECK_IN
   add constraint FK_CHECK_IN_CHECK_IN2_BUSINESS foreign key (BUSINESS_ID)
      references BUSINESS (BUSINESS_ID)
      on delete restrict on update restrict;

alter table HAS_CATEGORIE
   add constraint FK_HAS_CATE_HAS_CATEG_CATEGORI foreign key (CATEGORIE_ID)
      references CATEGORIE (CATEGORIE_ID)
      on delete restrict on update restrict;

alter table HAS_CATEGORIE
   add constraint FK_HAS_CATE_HAS_CATEG_BUSINESS foreign key (BUSINESS_ID)
      references BUSINESS (BUSINESS_ID)
      on delete restrict on update restrict;

alter table IS_FRIEND
   add constraint FK_IS_FRIEN_IS_FRIEND_USER foreign key (USER_ID)
      references "USER" (USER_ID)
      on delete restrict on update restrict;

alter table IS_FRIEND
   add constraint FK_IS_FRIEN_IS_FRIEND_USER2 foreign key (USE_USER_ID)
      references "USER" (USER_ID)
      on delete restrict on update restrict;

alter table REVIEW
   add constraint FK_REVIEW_HAS2_BUSINESS foreign key (BUSINESS_ID)
      references BUSINESS (BUSINESS_ID)
      on delete restrict on update restrict;

alter table REVIEW
   add constraint FK_REVIEW_WRITES_USER foreign key (USER_ID)
      references "USER" (USER_ID)
      on delete restrict on update restrict;

alter table WEATHER
   add constraint FK_WEATHER_RELATIONS_STATION foreign key (ID)
      references STATION (ID)
      on delete restrict on update restrict;

