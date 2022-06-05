from employee.models import Employee


class Pagination:
    def paginate(self, page = 1):
        all_records = Employee.objects.all().values()
        limit = 10
        start = (page-1) * limit
        end = start + limit
        total_record = Employee.objects.all().count()
        if total_record%limit == 0:
            total_page = total_record//limit
        else:
            total_page = total_record//limit + 1
        return all_records[start:end], total_page, total_record