import matplotlib.pyplot as plt
import pandas as pd

d=pd.read_csv("netflix_titles.csv")
d.dropna(subset=['show_id','type','title','director','cast','country','date_added','release_year','rating','duration','listed_in','description'],inplace=True)
type_count = d['type'].value_counts()

plt.figure(figsize=(15,5))

plt.subplot(1,4,1)
plt.bar(type_count.index, type_count.values, color=["orange","gold"])
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.grid(True)


country=d['country'].value_counts().head(5)

plt.subplot(1,4,2)
plt.pie(country,labels=country.index,autopct="%1.1f%%")
plt.title("Top 5 countries with most content")



genres=d['listed_in'].str.split(', ')
genres=genres.explode()
genres_count=genres.value_counts()
plt.subplot(1,4,3)
plt.bar(genres_count.index[:10], genres_count.values[:10])
plt.xlabel("Number of shows per genre")
plt.ylabel("Genres")
plt.xticks(rotation=45)
plt.grid(True)

release=d['release_year'].value_counts().sort_index()

plt.subplot(1,4,4)
plt.plot(release.index,release.values)
plt.title("Release by years")
plt.xlabel("Release")
plt.ylabel("Number of shows")
plt.grid(True)
plt.tight_layout()
plt.savefig("Data.png")
plt.show()

print("Numbers of tv shows and movies in netflix:",type_count)
print("Top countries with most content; ",country)
print("All types of genres content of netflix: ",genres_count)
print("Release by year: ",release)