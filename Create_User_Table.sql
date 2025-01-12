CREATE TABLE [CW2].[TrailUser] (
    [UserID]        INT           IDENTITY (1, 1) NOT NULL,
    [UserName]      NVARCHAR (50) NOT NULL,
    [Email_address] NVARCHAR (50) NOT NULL,
    [UserRole]      NVARCHAR (20) NOT NULL,
    CONSTRAINT [PK_USER_ID] PRIMARY KEY CLUSTERED ([UserID] ASC)
);