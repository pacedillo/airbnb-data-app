from mongoengine import*
from db.reviews import Reviews

class Listings(Document):
    listing_id = StringField(required=True, max_length=200)
    listing_url = StringField(required=True, max_length=200)
    scrape_id = StringField(required=True, max_length=200)
    last_scraped = BooleanField(required=True, default= False)
    name = StringField(required=True, max_length=200)
    summary = StringField(required=False)
    space = IntField(required=True)
    description = StringField(required=True)
    experiences_offered = StringField(required=False)
    neighborhood_overview = StringField(required=False)
    notes = StringField(required=False, max_length=600)
    transit = StringField(required=False, max_length=600)
    access = StringField(required=False, max_length=600)
    interaction = StringField(required=False, max_length=600)
    house_rules  = StringField(required=False, max_length=1000)
    thumbnail_url = URLField(required=False)
    medium_url = URLField(required=False)
    picture_url = URLField(required=True)
    xl_picture_url = URLField(required=False)
    host_id = StringField(required=True, max_length=200)
    host_url = StringField(required=True, max_length=200)
    host_name = StringField(required=True, max_length=200)
    host_since = DateField(required=True)
    host_location = StringField(required=True)
    host_about = StringField(required=False)
    host_response_time = StringField(required=True)
    host_response_rate = StringField(required=True)
    host_acceptance_rate = StringField(required=True)
    host_is_superhost = BooleanField(required=True)
    host_thumbnail_url = URLField(required=False)
    host_picture_url = URLField(required=False)
    host_neighbourhood = StringField(required=False)
    host_listings_count = IntField(required=True)
    host_total_listings_count = IntField(required=True)
    host_verifications = ListField(StringField(required=True))
    host_has_profile_pic = BooleanField(required=True)
    host_identity_verified = BooleanField(required=True)
    street = StringField(required=True, max_length=200)
    neighbourhood = StringField(required=False, max_length=200)
    neighbourhood_cleansed = StringField(required=True, max_length=200)
    neighbourhood_group_cleansed = StringField(required=False, max_length=200)
    city = StringField(required=True, max_length=200)
    state = StringField(required=True, max_length=200)
    zipcode = StringField(required=True, max_length=200)
    market = StringField(required=True, max_length=200)
    smart_location = StringField(required=True, max_length=200)
    country_code = StringField(required=True, max_length=200)
    country = StringField(required=True, max_length=200)
    latitude = StringField(required=True, max_length=200)
    longitude = StringField(required=True, max_length=200)
    is_location_exact = BooleanField(required=True)
    property_type = StringField(required=True, max_length=200)
    room_type = StringField(required=True, max_length=200)
    accommodates = IntField(required=True)
    bathrooms = IntField(required=True)
    bedrooms = IntField(required=True)
    beds = IntField(required=True)
    bed_type = StringField(required=True, max_length=200)
    amenities = ListField(StringField(required=True))
    square_feet = IntField(required=False)
    price = StringField(required=True, max_length=200)
    weekly_price = StringField(required=True, max_length=200)
    monthly_price = StringField(required=True, max_length=200)
    security_deposit = StringField(required=True, max_length=200)
    cleaning_fee = StringField(required=True, max_length=200)
    guests_included = StringField(required=True, max_length=200)
    extra_people = StringField(required=True, max_length=200)
    minimum_nights = IntField(required=True)
    maximum_nights = IntField(required=True)
    calendar_updated = StringField(required=True)
    has_availability = BooleanField(required=True)
    availability_30 = IntField(required=True)
    availability_60 = IntField(required=True)
    availability_90 = IntField(required=True)
    availability_365 = IntField(required=True)
    calendar_last_scraped = DateField(required=True)
    number_of_reviews = IntField(required=False)
    first_review = DateField(required=False)
    last_review  = DateField(required=False)
    review_scores_rating = IntField(required=False)
    review_scores_accuracy = IntField(required=False)
    review_scores_cleanliness = IntField(required=False)
    review_scores_checkin = IntField(required=False)
    review_scores_communication = IntField(required=False)
    review_scores_location = IntField(required=False)
    review_scores_value = IntField(required=False)
    review_list = ReferenceField(Reviews, required=True)
    requires_license = BooleanField(required=True)
    license = StringField(required=False)
    jurisdiction_names = StringField(required=False)
    instant_bookable = BooleanField(required=True)
    is_business_travel_ready = BooleanField(required=True)
    cancellation_policy = StringField(required=True, max_length=200)
    require_guest_profile_picture = BooleanField(required=False, default=False)
    require_guest_phone_verification = BooleanField(required=False, default=False)
    calculated_host_listings_count = IntField(required=False)
    reviews_per_month = IntField(required=False)
    first_available_date=DateField(required=False)
