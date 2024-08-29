class Review:
    def __init__(self, dish, rating, comments):
        self.dish = dish
        self.rating = rating  # Rating should be between 1 and 5
        self.comments = comments

    def __str__(self):
        return (f"Dish: {self.dish}\n"
                f"Rating: {self.rating}/5\n"
                f"Comments: {self.comments}\n")

class FoodReviewReport:
    def __init__(self):
        self.reviews = []

    def add_review(self, dish, rating, comments):
        # Validate the rating to be between 1 and 5
        if 1 <= rating <= 5:
            new_review = Review(dish, rating, comments)
            self.reviews.append(new_review)
            return f"Review for {dish} added successfully!"
        else:
            return "Rating must be between 1 and 5."

    def view_all_reviews(self):
        if not self.reviews:
            return "No reviews available."
        return "\n".join(str(review) for review in self.reviews)

    def generate_summary(self):
        if not self.reviews:
            return "No reviews available to summarize."

        total_reviews = len(self.reviews)
        average_rating = sum(review.rating for review in self.reviews) / total_reviews

        return (f"Total Reviews: {total_reviews}\n"
                f"Average Rating: {average_rating:.2f}/5\n")

# Example usage:

# When you define the __str__ method inside a class, you are essentially telling Python,
# "When someone tries to print this object, show this specific string instead."

# Creating an instance of FoodReviewReport
report = FoodReviewReport()

# Adding some reviews
print(report.add_review("Omakase", 5, "Amazing sushi, the best I've ever had!"))
print(report.add_review("Tonkotsu Ramen", 4, "Delicious broth and perfectly cooked noodles."))
print(report.add_review("Korean BBQ", 3, "Good but a bit overpriced."))

# Viewing all reviews
print("\nAll Reviews:\n")
print(report.view_all_reviews())

# Generating a summary report
print("\nSummary Report:\n")
print(report.generate_summary())
