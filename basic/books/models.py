from django.db import models
from django.contrib.auth.models import BaseUserManager

# Local
from authors.models import Author
from publishers.models import Publisher

TYPE_FANTASY, TYPE_HORROR, TYPE_SCI_FI, TYPE_ROMANCE = range(0, 4)
GENRE_TYPE = (
    (TYPE_FANTASY, 'Fantasy'),
    (TYPE_HORROR, 'Horror'),
    (TYPE_SCI_FI, 'Sci-fi'),
    (TYPE_ROMANCE, 'Romance'),
)


class BookGenre(models.Model):
    """
    Schema for book genres.
    TODO: Remember to delete book genre entries after deletion from book instances.
    """
    genre = models.SmallIntegerField(
        choices=GENRE_TYPE,
        default=None,
        null=False,
    )
    objects = BaseUserManager()

    @property
    def description(self):
        """Return string representation of our book genres"""
        if self.genre == TYPE_FANTASY:
            return 'By definition, fantasy is a genre that typically features the use of magic or other supernatural ' \
                   'phenomena in the plot, setting, or theme.'
        if self.genre == TYPE_HORROR:
            return 'Genre of fiction whose purpose is to create feelings of fear, dread, repulsion, and terror in the ' \
                   'audience—in other words, it develops an atmosphere of horror.'
        if self.genre == TYPE_SCI_FI:
            return 'Genre of speculative fiction that typically deals with imaginative and futuristic concepts such ' \
                   'as advanced science and technology, space exploration, time travel, parallel universes, ' \
                   'and extraterrestrial life.'
        if self.genre == TYPE_ROMANCE:
            return 'Romance is a narrative genre in literature that involves a mysterious, adventurous, or spiritual ' \
                   'story line where the focus is on a quest that involves bravery and strong values, not always a ' \
                   'love interest.'

    def __str__(self):
        """Return string representation of our book genres"""
        if self.genre == TYPE_FANTASY:
            return 'Fantasy'
        if self.genre == TYPE_HORROR:
            return 'Horror'
        if self.genre == TYPE_SCI_FI:
            return 'Sci-fi'
        if self.genre == TYPE_ROMANCE:
            return 'Romance'


class Book(models.Model):
    """
    Schema for book instances.
    """
    name = models.TextField(null=False)
    genre = models.ManyToManyField(BookGenre, related_name='books')
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name='books',
    )
    created_at = models.DateField(editable=False, auto_now=True)
    objects = BaseUserManager()

    def __str__(self):
        """Return string representation of our book"""
        return self.name
