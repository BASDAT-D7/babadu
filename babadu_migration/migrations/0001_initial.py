from django.db import migrations
from io import open

file_path = 'babadu_migration/babadu.sql'  # Path relatif dari file SQL
with open(file_path, 'r') as file:
    sql_content = file.read()

class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunSQL(sql_content),
    ]