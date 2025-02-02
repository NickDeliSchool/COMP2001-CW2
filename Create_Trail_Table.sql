CREATE TABLE [CW2].[Trail] (
    [Trail_ID]                        INT             IDENTITY (1, 1) NOT NULL,
    [Trail_Name]                      NVARCHAR (50)   NOT NULL,
    [Trail_Location]                  NVARCHAR (100)  NOT NULL,
    [Trail_Rating]                    FLOAT (53)      NULL,
    [Trail_Difficulty]                VARCHAR (20)    NULL,
    [Trail_Length_KM]                 INT             NULL,
    [Trail_Elevation_Gain_M]          INT             NULL,
    [Trail_Route_Type]                VARCHAR (20)    NULL,
    [Trail_Estimated_Finish_Time_Min] INT             NULL,
    [Trail_Summary]                   NVARCHAR (1500) NULL,
    [Trail_Description]               NVARCHAR (2000) NULL,
    [OwnerID]                         INT             NOT NULL,
    [Point1_lat]                      FLOAT (53)      NULL,
    [Point1_long]                     FLOAT (53)      NULL,
    [Point1_Desc]                     VARCHAR (30)    NULL,
    [Point2_lat]                      FLOAT (53)      NULL,
    [Point2_long]                     FLOAT (53)      NULL,
    [Point2_Desc]                     VARCHAR (30)    NULL,
    [Point3_lat]                      FLOAT (53)      NULL,
    [Point3_long]                     FLOAT (53)      NULL,
    [Point3_Desc]                     VARCHAR (30)    NULL,
    [Point4_lat]                      FLOAT (53)      NULL,
    [Point4_long]                     FLOAT (53)      NULL,
    [Point4_Desc]                     VARCHAR (30)    NULL,
    [Point5_lat]                      FLOAT (53)      NULL,
    [Point5_long]                     FLOAT (53)      NULL,
    [Point5_Desc]                     VARCHAR (30)    NULL,
    CONSTRAINT [PK_TRAIL_ID] PRIMARY KEY CLUSTERED ([Trail_ID] ASC),
    CONSTRAINT [FK_OwnerID] FOREIGN KEY ([OwnerID]) REFERENCES [CW2].[TrailUser] ([UserID])
);