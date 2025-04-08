import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='blog'
)
cursor=conn.cursor()

def get_tag_id(tag_name):
    cursor.execute("SELECT id FROM tags WHERE name = %s", (tag_name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    cursor.execute("INSERT INTO tags (name) VALUES (%s)", (tag_name,))
    conn.commit()
    return cursor.lastrowid

def create_post():
    title = input("Enter post title: ")
    content = input("Enter post content: ")
    tags_input = input("Enter comma-separated tags: ")
    tags = [tag.strip().lower() for tag in tags_input.split(",")]

    try:
        cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
        post_id = cursor.lastrowid

        for tag in tags:
            tag_id = get_tag_id(tag)
            cursor.execute("INSERT INTO post_tags (post_id, tag_id) VALUES (%s, %s)", (post_id, tag_id))

        conn.commit()
        print(" Post created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()

def view_all_titles():
    cursor.execute("SELECT title FROM posts")
    results = cursor.fetchall()
    print("\n Blog Post Titles:")
    for (title,) in results:
        print(f"- {title}")

def view_post_by_title():
    title = input("Enter the title of the post to view: ")
    cursor.execute("SELECT content FROM posts WHERE title = %s", (title,))
    result = cursor.fetchone()
    if result:
        print(f"Content:\n{result[0]}")
    else:
        print("Post not found.")

def search_by_tag():
    tag = input("Enter tag to search: ").lower()
    cursor.execute("""
        SELECT p.title 
        FROM posts p
        JOIN post_tags pt ON p.id = pt.post_id
        JOIN tags t ON pt.tag_id = t.id
        WHERE t.name = %s
    """, (tag,))
    results = cursor.fetchall()
    if results:
        print("\n Posts with this tag:")
        for (title,) in results:
            print(f"- {title}")
    else:
        print("No posts found with this tag.")

def main():
    while True:
        print("\n Blog Manager Menu:")
        print("1. Create a new post")
        print("2. View all post titles")
        print("3. View a post by title")
        print("4. Search posts by tag")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            create_post()
        elif choice == '2':
            view_all_titles()
        elif choice == '3':
            view_post_by_title()
        elif choice == '4':
            search_by_tag()
        elif choice == '5':
            print(" Exiting Blog Manager.")
            break
        else:
            print(" Invalid option. Please try again.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()