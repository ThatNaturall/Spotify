/****** Object:  Table [dbo].[Songs]    Script Date: 2024/02/18 23:23:55 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Songs](
	[Artist] [nvarchar](max) NOT NULL,
	[Song] [nvarchar](max) NOT NULL,
	[Duration_ms] [float] NOT NULL,
	[Explicit] [nvarchar](50) NOT NULL,
	[Year] [int] NOT NULL,
	[Popularity] [int] NOT NULL,
	[Danceability] [float] NOT NULL,
	[Energy] [float] NOT NULL,
	[Key] [int] NOT NULL,
	[loudness] [float] NOT NULL,
	[Mode] [int] NOT NULL,
	[Speechiness] [float] NOT NULL,
	[Acousticness] [float] NOT NULL,
	[Instrumentalness] [float] NOT NULL,
	[Liveness] [float] NOT NULL,
	[Valence] [float] NOT NULL,
	[Tempo] [float] NOT NULL,
	[Genre] [nvarchar](max) NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

