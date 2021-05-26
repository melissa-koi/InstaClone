from django.test import TestCase
from .models import Comment, Image, Profile, Likes
from django.contrib.auth.models import User


# Create your tests here.
class TestImageClass(TestCase):
    """
    Test class that test Images objects
    """

    # Setup method
    def setUp(self) -> None:
        self.new_user = User(username='Name', email='name@gmail.com')
        self.new_user.save()

        self.new_Image = Image(user=self.new_user, image='someimage.png', caption='pic of something')

    # Teardown method
    def tearDown(self) -> None:
        self.new_Image.save()
        self.new_Image.delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_Image, Image))

    # Testing saving Image
    def test_save_Image(self):
        self.new_Image.save_Image()
        Images = Image.objects.all()
        self.assertTrue(len(Images) > 0)

    # Testing deleting Image
    def test_delete_Image(self):
        self.new_Image.save_Image()
        Images = Image.objects.all()

        self.new_Image.delete_Image()

        self.assertTrue(len(Images) < 1)


class TestCommentClass(TestCase):
    """
    Test class to test comment class properties
    """

    # Setup method
    def setUp(self) -> None:
        self.new_user = User(usernname='Name', email='name@gmail.com')
        self.new_user.save()

        self.new_Image = Image(username=self.new_user, image='someimage.png', caption='caption')
        self.new_Image.save()

        self.new_comment = Comment(Image=self.new_Image, user=self.new_user, text='looksnice')

    # Teardown method
    def tearDown(self) -> None:
        self.new_comment.save()
        self.new_comment.delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(self.new_comment, Comment)

    # Testing saving comment
    def test_save_comment(self):
        self.new_comment.save_comment()
        comments = Comment.objects.all()

        self.assertTrue(len(comments) > 0)

    # Testing deleting comment
    def test_delete_comment(self):
        self.new_comment.save_comment()
        comments = Comment.objects.all()

        self.new_comment.delete_comment()
        self.assertTrue(len(comments) < 1)


class TestLikesClass(TestCase):
    """
    Test class to test likes class properties
    """

    # Setup
    def setUp(self) -> None:
        self.new_user = User(username='Name', email='name@gmail.com')
        self.new_user.save()

        self.new_Image = Image(user=self.new_user, image='someimage.png', caption='caption')
        self.new_Image.save()

        self.new_like = Likes(user=self.new_user, Image=self.new_Image, is_like=True)

    # Test instance
    def test_instance(self):
        self.assertTrue(self.new_like, Likes)

    # Testing saving like
    def test_save_like(self):
        self.new_like.save_like()
        likes = Likes.objects.all()
        self.assertTrue(len(likes) > 0)

    # Testing deleting like
    def test_delete_like(self):
        self.new_like.save_like()
        likes = Likes.objects.all()

        self.new_like.delete_like()
        self.assertTrue(len(likes) < 1)
