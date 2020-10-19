# -*- coding: latin-1 -*-
import unittest

' Test basic tokenization utilities.'
import unittest
from ..base import SentenceTokenizer, WordTokenizer
from ...base import Sequence
en_text = 'A Ukrainian separatist leader is calling on Russia to "absorb" the eastern region of Donetsk after Sunday\'s referendum on self rule. Self-declared Donetsk People\'s Republic leader Denis Pushilin urged Moscow to listen to the "will of the people". In neighbouring Luhansk, where a vote was also held, rebels declared independence. Ukraine, the EU and US have declared the referendums illegal but Russia says the results should be "implemented". Moscow has so far not commented on the call for Donetsk to become part of Russia but has appealed for dialogue between the militants and Kiev, with the participation of the Organisation for Security and Co-operation in Europe.\n'
ar_text = 'عبر أ�\xadد �\x82ادة ا�\x84�\x85ت�\x85رد�\x8a�\x86 ا�\x84�\x85�\x88ا�\x84�\x8a�\x86 �\x84ر�\x88س�\x8aا �\x81�\x8a أ�\x88�\x83را�\x86�\x8aا ع�\x86 �\x85سا�\x86دت�\x87 �\x84�\x81�\x83رة ا�\x84�\x88�\xadدة �\x85ع ر�\x88س�\x8aا �\x81�\x8a أع�\x82اب ا�\x84إع�\x84ا�\x86 ع�\x86 �\x86تائج ا�\x84است�\x81تاء ا�\x84�\x85ث�\x8aر �\x84�\x84جد�\x84 �\x81�\x8a شر�\x82 ا�\x84ب�\x84اد. �\x88�\x82ا�\x84 ر�\x88�\x85ا�\x86 �\x84�\x8aاج�\x8a�\x86�\x8c رئ�\x8aس �\x84ج�\x86ة ا�\x84�\x85ت�\x85رد�\x8a�\x86 �\x84�\x84ا�\x86تخابات �\x81�\x8a د�\x88�\x86�\x8aتس�\x83 إ�\x86 ا�\x84ا�\x86ض�\x85ا�\x85 �\x84ر�\x88س�\x8aا "�\x82د �\x8a�\x83�\x88�\x86 خط�\x88ة �\x85�\x86اسبة".\n'
ja_text = '�\x82\x84�\x81��\x81\x9f!'

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.en_seq = Sequence(en_text)
        self.ar_seq = Sequence(ar_text)
        self.ja_seq = Sequence(ja_text)
        self.en_sent = SentenceTokenizer(locale='en')
        self.ar_sent = SentenceTokenizer(locale='ar')
        self.ja_sent = SentenceTokenizer(locale='ja')
        self.en_word = WordTokenizer(locale='en')
        self.ar_word = WordTokenizer(locale='ar')
        self.ja_word = WordTokenizer(locale='ja')
        self.en_sents = self.en_sent.transform(self.en_seq)
        self.ar_sents = self.ar_sent.transform(self.ar_seq)
        self.ja_sents = self.ja_sent.transform(self.ja_seq)
        self.en_words = self.en_word.transform(self.en_seq)
        self.ar_words = self.ar_word.transform(self.ar_seq)
        self.ja_words = self.ja_word.transform(self.ja_seq)

    def tearDown(self):
        pass

    def test_sentences_count(self):
        ' Sentence segmentation produces correct number of sentences.'
        self.assertEqual(5, len(self.en_sents))
        self.assertEqual(2, len(self.ar_sents))
        self.assertEqual(1, len(self.ja_sents))

    def test_redundant_idx(self):
        ' Test if there are redundant indices.'
        self.assertEqual(len(self.en_sents.idx), len(set(self.en_sents.idx)))
        self.assertEqual(len(self.ar_sents.idx), len(set(self.ar_sents.idx)))
        self.assertEqual(len(self.ja_sents.idx), len(set(self.ja_sents.idx)))
        self.assertEqual(len(self.en_words.idx), len(set(self.en_words.idx)))
        self.assertEqual(len(self.ar_words.idx), len(set(self.ar_words.idx)))
        self.assertEqual(len(self.ja_words.idx), len(set(self.ja_words.idx)))

    def test_boundaries(self):
        ' Sentence boundaries should be also word boundaries.'
        self.assertTrue(set(self.en_sents.idx).issubset(set(self.en_words.idx)))
        self.assertTrue(set(self.ar_sents.idx).issubset(set(self.ar_words.idx)))
        self.assertTrue(set(self.ja_sents.idx).issubset(set(self.ja_words.idx)))

    def test_transformations_equal(self):
        ' Word toeknization over text is equal to over sentences.'
        idx1 = self.en_words.idx
        idx2 = self.en_word.transform(self.en_sents).idx
        self.assertListEqual(idx1, idx2)
        idx1 = self.ar_words.idx
        idx2 = self.ar_word.transform(self.ar_sents).idx
        self.assertListEqual(idx1, idx2)
        idx1 = self.ja_words.idx
        idx2 = self.ja_word.transform(self.ja_sents).idx
        self.assertListEqual(idx1, idx2)
if (__name__ == '__main__'):
    unittest.main()

