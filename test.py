#https://stackoverflow.com/questions/73023173/why-do-i-cant-extract-data-from-response-using-grequests
import grequests
import time

start_time = time.time()


sites = ['https://facebook.com' for x in range(5)]
data = {'a': 'b'}

responses = [grequests.get(u, data=data) for u in sites]

# wait for all results
responses = grequests.map(responses)

for response in responses:
    print('response:', response)
    print('status_code:', response.status_code)
    print('text:', response.text)

print("--- %s seconds ---" % (time.time() - start_time))