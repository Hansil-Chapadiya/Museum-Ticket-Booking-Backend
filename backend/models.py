from djongo import models
from bson import ObjectId

class Museums(models.Model):
    _id = models.ObjectIdField(auto_created=True, primary_key=True, default=ObjectId)
    museum_name = models.TextField(unique=True)
    description = models.TextField()
    dwell_time = models.IntegerField()
    adult_price = models.IntegerField()
    child_price = models.IntegerField()
    hero_image = models.TextField()

    def __str__(self):
        return self.museum_name


'''
const TicketSchema: Schema<ITicket> = new Schema(
  {
    museum_id: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "Museum",
      required: true
    },
    user_id: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
      required: true
    },
    expire_time: {
      type: Date,
      required: true
    },
    no_of_adults: {
      type: Number,
      required: true
    },
    no_of_child: {
      type: Number,
      required: true
    },
    total_price: {
      type: Number,
      required: true
    },
    checker_id: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "Ticket_Checker",
      required: false // Optional reference
    },
    date_time: {
      type: Date,
      required: true
    }

'''

class Ticket(models.Model):
    _id = models.ObjectIdField(auto_created=True, primary_key=True, default=ObjectId)
    museum_id = models.ObjectIdField()
    user_id = models.ObjectIdField()
    expire_time = models.DateTimeField()
    no_of_adults = models.IntegerField()
    no_of_child = models.IntegerField()
    total_price = models.IntegerField()
    checker_id = models.ObjectIdField()
    created_at = models.DateTimeField(auto_now_add=True)