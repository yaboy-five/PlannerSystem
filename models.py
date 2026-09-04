from database import get_connection

# add user
def add_user(name, email):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Users (Name, Email)
        VALUES (?, ?)
    """, name, email)

    connection.commit()
    connection.close()

# --- Activities --- 

# view activities
def get_activities():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            Activities.ActivityID, 
            Activities.ActivityName, 
            Activities.ActivityDate, 
            Activities.ActivityType, 
            Activities.Status, 
            Activities.UserID, 
            Users.Name 
        FROM Activities 
        INNER JOIN Users 
            ON Activities.UserID = Users.UserID 
        ORDER BY 
            Activities.ActivityDate DESC
    """)

    activities = cursor.fetchall()

    connection.close()

    return activities

# add activity
def add_activity(activity_name, activity_date, activity_type, status, user_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Activities (
            ActivityName,
            ActivityDate, 
            ActivityType, 
            Status, 
            UserID
        )
        VALUES (?, ?, ?, ?, ?),
    """,
    activity_name, activity_date, activity_type, status, user_id)

    connection.commit()
    connection.close()

# update activity
def update_activity(activity_id, activity_name, activity_date, activity_type, status, user_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE Activities
        SET 
            ActivityName = ?,
            ActivityDate = ?, 
            ActivityType = ?, 
            Status = ?, 
            UserID = ? 
        WHERE ActivityID = ? """, 
        activity_name, activity_date, activity_type, status, user_id, activity_id)

    connection.commit()
    connection.close()

# delete activity
def delete_activity(activity_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM Activities
        WHERE ActivityID = ?""",
        activity_id)

    connection.commit()
    connection.close()

# --- report ---

# total users
def get_total_users():

    connection = get_connection() 
    cursor = connection.cursor() 

    cursor.execute(""" 
        SELECT COUNT(*) 
        FROM Users """) 

    total = cursor.fetchone()[0] 
    connection.close() 
    return total