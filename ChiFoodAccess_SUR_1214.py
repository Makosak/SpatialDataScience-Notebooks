{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf460
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww28600\viewh16500\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 ##########################\
# Food Access Change in Chicago From 2011 to 2014\
# Author: Marynia Kolak\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 ##########################\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \
import pysal\
db = pysal.open("/Users/Masia/Desktop/FA_clip/FA_Panel_1214.dbf")\
\
## Queen-Contiguity Spatial Weight generated\
w = pysal.queen_from_shapefile("/Users/Masia/Desktop/FA_clip/FA_Panel_1214.shp")\
w.transform='r'\
\
## Census Tract Average Network Distance Miles to Supermarkets \
y_var = ['MEANMI_11','MEANMI_14']\
\
## Potential explanatory variables: Population, White%, Black%, Hispanic$, Unemployed,\
## Childhood Poverty%, Overall Poverty%\
x_var=[['Pop2012','Wht12P','Blk12P','Hisp12P','UnEmpl12','ChldPvty12','PvtyPrc12'],\
       ['Pop2014','Wht14P','Blk14P','Hisp14P','UnEmpl14','ChldPvty14','PvtyPrc14']]\
\
bigy,bigX,bigyvars,bigXvars = pysal.spreg.sur_utils.sur_dictxy(db,y_var,x_var)\
\
## The following doesn't work, though is in the existing documentation:\
## reg = SUR(bigy,bigX,w=w,name_bigy=bigyvars,name_bigX=bigXvars,spat_diag=True,name_ds="nat")\
\
reg = pysal.spreg.sur.SUR(bigy,bigX,w=w,name_bigy=bigyvars,name_bigX=bigXvars,\
                          spat_diag=True,name_ds="nat",name_w=w)\
\
print(reg.summary)}