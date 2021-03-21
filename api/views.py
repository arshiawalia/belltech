
from django.http import HttpRequest,HttpResponse
import csv

from django.http.response import JsonResponse


class CityDetails:
	def ViewData(request,station=None):
		data={}
		station_details=[]
		# read file
		with open(r'C:\Users\arshi\OneDrive\Desktop\Sub_Urban_Rail_Chennai.csv') as file:
			reader = csv.DictReader(file)
			line_count=1
			if station:
				for row in reader:
					station_details.append([row])
				return station_details
			for row in reader:
				data[line_count]=row 
				line_count+=1

		return JsonResponse(data)

	def StationDetails(request):
		station_details=[]
		# query parameter :qp
		qp = request.GET.get('station')
		# fetch data from csv
		data = CityDetails.ViewData(request,qp)

		for i in data:
			# if station exists
			if i[0]["Station"] == qp:
				station_details.append(i)
			else:
				#throw err
				pass
		return HttpResponse(station_details)

	def Distance(request):

		a,b=None,None
		# from,to stations :query param's
		_from = request.GET.get('from')
		_to = request.GET.get("to")

		# if stations not given : throw err
		if not _from or not _to:
			if not _from and not _to :
				return HttpResponse('<h1>Stations Not Given </h1>')
				
			elif not _from :
				return HttpResponse('<h1>Departure Station Not Given </h1>')

			elif not _to:
				return HttpResponse('<h1>Destination Station Not Given  </h1>')

		# stations from and to given

		data = CityDetails.ViewData(request,_from)
		
		for i in data:
			# if stations are present in the csv
			if i[0]["Station"] == _from:
				a = i[0]["Distance in Kms"]
			
			if i[0]["Station"] == _to:
				b = i[0]["Distance in Kms"]
			
			# else:
				# do something
				

			
			if a and b:
				return HttpResponse('<h1>Distance between {} and {} is : {} km </h1>'.format(_from,_to,abs(float(a)-float(b))))
			# else:
			# 	return HttpResponse('<h1>Err</h1>{}{}'.format(a,b))
	
		