### Notes
A note-taking & planning app built by Draylar and teokafor for our final in Software Development II.

### Application Overview

This application consists of a front-end and back-end. The back-end handles syncing and storing data for users,
while the front-end displays information and allows users to edit their data.

### Requests

`GET /api/all`

Returns all notes & plans for the given user.

**Request Data**:

id: username of the owner of the data to retrieve

---

`GET /api/plans`

Returns all plans for the given user.

**Request Data**:

id: username of the owner of the data to retrieve

---

`GET /api/notes`

Returns all notes for the given user.

**Request Data**:

id: username of the owner of the data to retrieve

---

`GET /api/individual`

Returns a specific note or schedule for the given user.

**Request Data**:

id: username of the owner of the data to retrieve
entry_id: ID of the entry to retrieve

---

`GET /api/hash/`

Returns the hash of the plan or schedule with the given ID.

**Request Data**:

id: username of the owner of the data to retrieve
entry_id: ID of the entry to retrieve the hash of

---

`POST /api/update/`

Updates the given schedule or note.

**Request Data**:

id: username of the owner of the data to retrieve
entry_id: ID of the entry to retrieve the hash of
contents: Contents to update stored values to

---
