CREATE TABLE CW2.Trail(
Trail_ID INT IDENTITY NOT NULL,
OwnerID INT NOT NULL,
Trail_Name NVARCHAR(50) NOT NULL,
Trail_Rating FLOAT,
Trail_Difficulty VARCHAR(20),
Trail_Length_KM INT,
Trail_Elevation_Gain_M INT,
Trail_Route_Type VARCHAR(20),
Trail_Estimated_Finish_Time_Min INT,
Trail_Introduction NVARCHAR(1000),
Trail_Description NVARCHAR(1500),
Location_ID INT,

CONSTRAINT FK_LOCATION_ID FOREIGN KEY(Location_ID) REFERENCES CW2.Location (Location_ID),
CONSTRAINT FK_OwnerID FOREIGN KEY(OwnerID) REFERENCES CW2.TrailUser (UserID),
CONSTRAINT PK_TRAIL_ID PRIMARY KEY(Trail_ID)
)