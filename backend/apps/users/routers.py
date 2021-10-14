from fastapi import APIRouter

router = APIRouter(
    prefix="/apps/users"
)

async def check_user_exist(email:str):
    # bool function to check if user email already exists in the db 


async def signup_data(firstname:str, lastname:str, email:str, password:str):
    # add user details in the db 




@router.get("/signup")
async def signup(firstname:str, lastname:str, email:str, password:str):
    if '@' not in email:
        return {"status": "Email ID Invalid"}

    user_exist = await check_user_exist(email)
    if user_exist==0:
        user = {"user_details": [
            {
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
                "password": password
            }
        ]}
        # call signup_data function
        # new_user = await db["users"].insert_one(user)
        return {"status": "Signed up."}
    else:
        return {"status": "Account already exists, please consider signing in."}