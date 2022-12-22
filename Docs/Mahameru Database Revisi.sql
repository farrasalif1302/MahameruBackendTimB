CREATE TABLE [user] (
  [_id] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [nickname] String NOT NULL,
  [no_tlp] VARCHAR(12) NOT NULL,
  [pin] VARCHAR(40) NOT NULL,
  [name] VARCHAR(20) NOT NULL DEFAULT '',
  [created_at] DATETIME NOT NULL,
  [updated_at] DATETIME NOT NULL,
  [channel_id] INT
)
GO

CREATE TABLE [user_contact] (
  [user_id] INT NOT NULL,
  [_id] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [user_id_2] INT,
  [contact_id] INT,
  [created_at] DATETIME NOT NULL,
  [updated_at] DATETIME NOT NULL
)
GO

CREATE TABLE [channel] (
  [_id] INT PRIMARY KEY NOT NULL,
  [user_id] INT,
  [member_id] int,
  [name] VARCHAR(50) NOT NULL,
  [description] VARCHAR(50),
  [created_at] DATETIME,
  [updated_at] DATETIME
)
GO

CREATE TABLE [chat] (
  [_id] INT,
  [To_user] INT,
  [From_user] INT,
  [message] text,
  [_date] DATETIME,
  [status] boolean
)
GO

CREATE TABLE [Friend Profile] (
  [user_id] INT,
  [user_contact] INT,
  [friend_contact] INT,
  [contact_id] INT,
  [created_at] DATETIME,
  [updated_at] DATETIME,
  [phone number] VARCHAR
)
GO

CREATE UNIQUE INDEX [no_tlp_UNIQUE] ON [user] ("no_tlp")
GO

CREATE UNIQUE INDEX [nickname_UNIQUE] ON [user] ("nickname")
GO

ALTER TABLE [user] ADD FOREIGN KEY ([_id]) REFERENCES [user_contact] ([user_id_2])
GO

ALTER TABLE [user] ADD FOREIGN KEY ([_id]) REFERENCES [user_contact] ([user_id])
GO

ALTER TABLE [channel] ADD FOREIGN KEY ([user_id]) REFERENCES [user] ([_id])
GO

ALTER TABLE [channel] ADD FOREIGN KEY ([member_id]) REFERENCES [user] ([_id])
GO

ALTER TABLE [channel] ADD FOREIGN KEY ([_id]) REFERENCES [user] ([channel_id])
GO

ALTER TABLE [chat] ADD FOREIGN KEY ([To_user]) REFERENCES [user] ([_id])
GO

ALTER TABLE [chat] ADD FOREIGN KEY ([From_user]) REFERENCES [user] ([_id])
GO

ALTER TABLE [user] ADD FOREIGN KEY ([_id]) REFERENCES [Friend Profile] ([user_id])
GO
