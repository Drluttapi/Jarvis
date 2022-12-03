from pydoc import cli
import wolframalpha
client=wolframalpha.Client("KYAU62-63QGP34EKH")
result = client.query('weather forcast in kottayam').results
print(next(result).text)