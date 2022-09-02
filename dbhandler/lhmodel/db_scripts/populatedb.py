import json
from core.models import User, UserDetails, Role, ArtistInfo, BankDetails, Artifact, Cart
import os
import lhmodel.settings.test as settings

def make_users(fullbody):
	for data in fullbody["users"]:
		
		user = User.objects.create(
			email = data["email"],
			phone = data["phone"],
			password = data["password"],
			first_name = data["first_name"],
			last_name = data["last_name"],
		)

		role_st = data["role"]
		role = Role.objects.get(role=role_st)
		if role_st != "user":
			bank_details = BankDetails.objects.create(
				ifsc_code = data["bank_details"]["ifsc_code"],
				bank_name = data["bank_details"]["bank_name"],
				account_number = data["bank_details"]["account_number"]
			)
			bank_details.save()

			artist_info = ArtistInfo.objects.create(
				subdomain = data["subdomain"],
				description = data["description"],
				bank_details = bank_details
			)
			artist_info.save()

			user_details = UserDetails.objects.create(
				role = role,
				dp_s3_url = data["dp_s3_url"],
				artist_info = artist_info
			)

			user_details.save()

			user.details = user_details
			
		user.save()
	return 0
	


def make_artifacts(data):
	for afdata in data["artifacts"]:
		artist_email = afdata["artist_email"]
		artist = User.objects.get(email=artist_email)

		artifact = Artifact.objects.create(
			artist=artist,
			title=afdata["title"],
			description=afdata["description"],
			price=afdata["price"],
			is_exclusive=afdata["is_exclusive"],
		)
		artifact.save()
	return 0
	

def make_cart(data):
	for cdata in data["cart"]:
		buyer_email = cdata["buyer_email"]
		buyer = User.objects.get(email=buyer_email)
		artifact_id = cdata["artifact_id"]
		artifact = Artifact.objects.get(id = artifact_id)
		cart = Cart.objects.create(
			buyer = buyer,
			artifact = artifact
		)
		cart.save()
	return 0

	

def populatedb():
	data = None
	print(os.getcwd())
	with open(os.path.join(os.path.dirname(settings.BASE_DIR),'db_scripts', 'testdata.json')) as f:
		data = json.load(f)
	
	if make_users(data) != 0:
		print("make user broke. please fix it first")
		return 1
	
	if make_artifacts(data) != 0:
		print("make artifact broke. please fix it first")
		return 2

	if make_cart(data) != 0:
		print("make cart broke. please fix it first")
		return 3
	
	return 0
	
	
if __name__=='__main__':
	populatedb()

	




