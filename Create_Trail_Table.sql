CREATE TABLE CW2.Trail(
Trail_ID INT IDENTITY NOT NULL,
Trail_Name NVARCHAR(50) NOT NULL,
Trail_Location NVARCHAR(100) NOT NULL,
Trail_Rating FLOAT,
Trail_Difficulty VARCHAR(20),
Trail_Length_KM INT,
Trail_Elevation_Gain_M INT,
Trail_Route_Type VARCHAR(20),
Trail_Estimated_Finish_Time_Min INT,
Trail_Summary NVARCHAR(1000),
Trail_Description NVARCHAR(1500),
OwnerID INT NOT NULL,
Pt1_Lat FLOAT,
Pt1_Long FLOAT,
Pt1_Desc NVARCHAR(20),
Pt2_Lat FLOAT,
Pt2_Long FLOAT,
Pt2_Desc NVARCHAR(20),
Pt3_Lat FLOAT,
Pt3_Long FLOAT,
Pt3_Desc NVARCHAR(20),
Pt4_Lat FLOAT,
Pt4_Long FLOAT,
Pt4_Desc NVARCHAR(20),
Pt5_Lat FLOAT,
Pt5_Long FLOAT,
Pt5_Desc NVARCHAR(20)


CONSTRAINT FK_OwnerID FOREIGN KEY(OwnerID) REFERENCES CW2.TrailUser (UserID),
CONSTRAINT PK_TRAIL_ID PRIMARY KEY(Trail_ID)
)