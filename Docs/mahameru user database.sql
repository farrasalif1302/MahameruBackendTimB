CREATE TABLE [user] (
  [ID] INT PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [nickname] String NOT NULL,
  [no_tlp] VARCHAR(12) NOT NULL,
  [pin] VARCHAR(40) NOT NULL,
  [name] VARCHAR(20) NOT NULL DEFAULT '',
  [created_at] DATETIME NOT NULL,
  [updated_at] DATETIME NOT NULL,
  [contact_id] INT
)
GO

CREATE TABLE [user_contact] (
  [user_id] INT NOT NULL,
  [contact_id] INT PRIMARY KEY,
  [created_at] DATETIME NOT NULL,
  [updated_at] DATETIME NOT NULL
)
GO

CREATE UNIQUE INDEX [no_tlp_UNIQUE] ON [user] ("no_tlp")
GO

CREATE UNIQUE INDEX [nickname_UNIQUE] ON [user] ("nickname")
GO

ALTER TABLE [user_contact] ADD FOREIGN KEY ([contact_id]) REFERENCES [user] ([contact_id])
GO

ALTER TABLE [user] ADD FOREIGN KEY ([ID]) REFERENCES [user_contact] ([user_id])
GO
