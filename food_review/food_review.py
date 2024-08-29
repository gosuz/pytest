class FoodReview:
    def __init__(self, name, country, rating=0, comment="n/a"):
        self.name = name #str
        self.country = country #str
        self.rating = rating #int
        self.comment = comment #str

    def description(self):
        return(f"{self.name} comes from {self.country}, and I gave it a {self.rating}. Here are the Notes: {self.comment}")

    def update_rating(self, new_rating):
        if new_rating >= 0 and new_rating <= 5:
            self.rating = new_rating

    def update_comment(self, new_comment):
        self.comment = new_comment


pho = FoodReview("Pho", "Vietnam", 5, "My go to cuisine")

ramen = FoodReview("Ramen", "Japan", 3)

print(ramen.description())

ramen.comments = "I like it. But its a bit over rated imo."

print(ramen.comments)


ramen.update_rating(4)
ramen.update_comment("Actually, after eating Tsukemen, its a lot better.")
print(ramen.description())
