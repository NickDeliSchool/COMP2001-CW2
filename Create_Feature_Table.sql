CREATE TABLE [CW2].[Feature] (
    [Feature_ID]   INT           IDENTITY (1, 1) NOT NULL,
    [Feature_Name] NVARCHAR (30) NOT NULL,
    [Trail_ID]     INT           NOT NULL,
    CONSTRAINT [PK_FEATURE_ID] PRIMARY KEY CLUSTERED ([Feature_ID] ASC),
    CONSTRAINT [FK_Trail_ID] FOREIGN KEY ([Trail_ID]) REFERENCES [CW2].[Trail] ([Trail_ID])
);