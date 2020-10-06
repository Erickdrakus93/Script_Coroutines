import jwt
import graphene

# The objective is Create the uid to generate access to the rest of the api
# Todo: Here the string that represents the db is mutable so we need
SECRET_KEY = ''  # This secret-key is generated from a subroutine that generates it
db = 'the Odoo_database_name'  # Here we need to create the user as we can see


# Here we need to use the API of Odoo to create the calling methods coherent with our logic inside


def generate_token(name, user_id):
    """In this example we can see the generate in a particular form of the token
       Here we don't need to create the password in the payload decode for the other side of the decoding form as we can
           see """
    token = jwt.encode({'name': name, 'id': user_id},
                       SECRET_KEY, algorithm='HS256')
    return token


def token_to_string(token):
    """This function is to convert the token to bytes in text as we can note"""
    return token.decode('utf-8')


class CreateAuth(graphene.Mutation):
    """ This mutation is to create the token for the Authorization """

    class Arguments:
        mame = graphene.String(required=True)
        password = graphene.String(required=True)
        user_id = graphene.Int()

    token = graphene.String()

    # This will be a classmethod in the Odoo_graphql_base
    # This authentication needs db name

    def mutate(self, info, username, password):
        env = info["env"]  # This is the environment to create the next part of the use
        uid = env["res.users"].authenticate(db, username, password, {})  # This is the manner to create the user_db
        pre_token = generate_token(username, uid)
        token = token_to_string(pre_token)
        # agent
        if env["res.users"].check(db, uid, password):  # This is the logic inside of the main functions of the manner
            # to call inside
            return CreateAuth(token=token)
        else:
            raise ConnectionError  # Here we define the next part of an authentication error


class Mutation(graphene.ObjectType):
    createAuth = CreateAuth.Field()


schema = graphene.Schema(mutation=Mutation)  # This is the object to connect the data as we can see
