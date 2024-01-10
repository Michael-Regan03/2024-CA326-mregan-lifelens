from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CSVUploadSerializer
from .models import DailyActivities
import csv, io

class DailyActivitiesCSVUpload(APIView):
    def post(self, request, format=None):
        serializer = CSVUploadSerializer(data=request.data)

        if serializer.is_valid():
            csv_file = serializer.validated_data['file']
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)  # Skip the header row

            # Process CSV file and save each row to the database
            for row in csv.reader(io_string, delimiter=',', quotechar="|"):
                DailyActivities.objects.create(
                    ts=float(row[0]),
                    action=row[1],
                    actionOption=int(row[2]),
                    actionSub=row[3] if row[3] else None,
                    actionSubOption=float(row[4]) if row[4] else None,
                    condition=row[5],
                    conditionSub1Option=float(row[6]) if row[6] else None,
                    conditionSub2Option=float(row[7]) if row[7] else None,
                    place=row[8],
                    emotionPositive=int(row[9]),
                    emotionTension=int(row[10]),
                    activity=int(row[11]),
                )

            return Response({"message": "CSV file processed successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)