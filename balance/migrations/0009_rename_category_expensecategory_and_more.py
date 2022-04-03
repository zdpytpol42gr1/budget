# Generated by Django 4.0.3 on 2022-04-02 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0008_remove_expense_user_delete_income'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='ExpenseCategory',
        ),
        migrations.AlterModelOptions(
            name='expensecategory',
            options={'verbose_name_plural': 'Expense Categories'},
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='category',
            new_name='expense_category',
        ),
        migrations.RenameField(
            model_name='expensecategory',
            old_name='category_name',
            new_name='expense_category_name',
        ),
    ]
