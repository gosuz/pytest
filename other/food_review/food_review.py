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



# This is the Class
class Noodles:
    def __init__(self, name, country, spice=0, rating=0, comments=[]):
        self.name = name
        self.country = country
        self.spice = spice
        self.rating = rating
        self.comments = comments

    def __str__(self):
        return f"{self.name} is a noodle dish from {self.country}. I give it a Rating:{self.rating}"

    def update_rating(self, new_score):
        self.rating = new_score

    def add_comments(self, comment):
        self.comments.append(comment)

    def show_comments(self):
        if len(self.comments) == 0:
            return "No Comments Listed"
        else:
            listed_comments = '\n'.join(self.comments)
            return listed_comments

# These are Instants

pho = Noodles('Pho', 'Vietnam', 3, 10,)


pho.add_comments("Pho is the best noodle dish in the world.")
pho.add_comments("I agree. Nothing is better")


naengmyun = Noodles("Naengmyun", "Korea", 0, 9)
print(naengmyun)

naengmyun.add_comments("Great during summer. Meh during winter")
naengmyun.update_rating(7)

print(naengmyun)
