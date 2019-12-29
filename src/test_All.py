import pytest
from SeqADT import *
from SALst import *
from DCapALst import *


class TestSeqADT:
    def test_next(self):
        s = SeqADT([1, 2, 3])
        s.next()
        s.next()
        assert s.next() == 3

    def test_empty_next(self):
        s = SeqADT([])
        with pytest.raises(StopIteration):
            s.next()

    def test_start(self):
        s = SeqADT([1, 2, 3])
        s.next()
        s.next()
        s.start()
        assert s.next() == 1

    def test_end(self):
        s = SeqADT([1, 2])
        s.next()
        s.next()
        assert s.end() == True

    def test_end_2(self):
        s = SeqADT([1, 2])
        assert s.end() == False


class TestDCapALst:

    DCapALst.init()

    def test_add(self):
        DCapALst.add(DeptT.civil, 20)
        assert DCapALst.s == [(DeptT.civil, 20)]

    def test_add_2(self):
        with pytest.raises(KeyError):
            DCapALst.add(DeptT.civil, 20)

    def test_remove(self):
        DCapALst.remove(DeptT.civil)
        assert DCapALst.s == []

    def test_remove_2(self):
        with pytest.raises(KeyError):
            DCapALst.remove(DeptT.civil)

    def test_elm(self):
        assert DCapALst.elm(DeptT.civil) == False

    def test_elm_2(self):
        DCapALst.add(DeptT.civil, 20)
        assert DCapALst.elm(DeptT.civil) == True

    def test_capacity(self):
        assert DCapALst.capacity(DeptT.civil) == 20

    def test_capacity_2(self):
        with pytest.raises(KeyError):
            DCapALst.capacity(DeptT.electrical)


class TestSALst:
    SALst.init()

    def test_add(self):
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), False)
        SALst.add("lastf", sinfo1)
        assert SALst.s == [("lastf", sinfo1)]

    def test_add_2(self):
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), False)
        with pytest.raises(KeyError):
            SALst.add("lastf", sinfo1)

    def test_remove(self):
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), False)
        SALst.remove("lastf")
        assert SALst.s == []

    def test_remove_2(self):
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), False)
        with pytest.raises(KeyError):
            SALst.remove("lastf")

    def test_elm(self):
        assert SALst.elm("firstf") == False

    def test_elm_2(self):
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), False)
        SALst.add("lastf", sinfo1)
        assert SALst.elm("lastf") == True

    def test_info(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), False)
        SALst.add("lastf", sinfo1)
        assert SALst.info("lastf") == sinfo1

    def test_info_2(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), False)
        SALst.add("lastf", sinfo1)
        with pytest.raises(KeyError):
            assert SALst.info("test")

    def test_sort(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                               SeqADT([DeptT.civil, DeptT.chemical]), False)

        sinfo2 = SInfoT("Zayed", "Sheet", GenT.male, 10.5,
                               SeqADT([DeptT.software, DeptT.chemical]), True)

        sinfo3 = SInfoT("Dom", "Buswoki", GenT.male, 11.0,
                               SeqADT([DeptT.software, DeptT.chemical]), False)

        sinfo4 = SInfoT("Farzad", "Valki", GenT.male, 1.0,
                               SeqADT([DeptT.software, DeptT.chemical]), False)


        SALst.add("sheetz", sinfo2)
        SALst.add("buswoki", sinfo3)
        SALst.add("lastf", sinfo1)
        SALst.add("valkif", sinfo4)

        assert SALst.sort(lambda t: not t.freechoice and t.gpa >= 4.0) == \
               ["lastf","buswoki"]

    def test_sort_2(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                               SeqADT([DeptT.civil, DeptT.chemical]), False)

        sinfo2 = SInfoT("Zayed", "Sheet", GenT.male, 10.5,
                               SeqADT([DeptT.software, DeptT.chemical]), True)

        sinfo3 = SInfoT("Dom", "Buswoki", GenT.male, 11.0,
                               SeqADT([DeptT.software, DeptT.chemical]), False)

        sinfo4 = SInfoT("Farzad", "Valki", GenT.male, 1.0,
                               SeqADT([DeptT.software, DeptT.chemical]), False)


        SALst.add("sheetz", sinfo2)
        SALst.add("buswoki", sinfo3)
        SALst.add("lastf", sinfo1)
        SALst.add("valkif", sinfo4)

        assert SALst.sort(lambda t: t.gpa >= 0) == \
               ["lastf", "buswoki", "sheetz", "valkif"]

    def test_sort_3(self):
        SALst.init()
        assert SALst.sort(lambda t: t.gpa >= 0) == []

    def test_average(self):
        with pytest.raises(ValueError):
            assert SALst.average(lambda x: x.gender == GenT.male)

    def test_average_2(self):
        sinfo5 = SInfoT("Cat", "Gonzal", GenT.female, 8,
                               SeqADT([DeptT.software, DeptT.chemical]), True)
        sinfo6 = SInfoT("Pedram", "Yazdinia", GenT.male, 8,
                               SeqADT([DeptT.software, DeptT.chemical]), False)
        sinfo3 = SInfoT("Dom", "Buswoki", GenT.male, 10,
                               SeqADT([DeptT.software, DeptT.chemical]), False)

        SALst.add("gonzalc", sinfo5)
        SALst.add("yazdiniap", sinfo6)
        SALst.add("buswoki", sinfo3)

        assert SALst.average(lambda x: x.gender == GenT.male) == 9

    def test_allocate(self):
        SALst.init()
        DCapALst.init()
        DCapALst.add(DeptT.civil,5)
        DCapALst.add(DeptT.software, 4)
        DCapALst.add(DeptT.electrical, 3)
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                               SeqADT([DeptT.civil, DeptT.chemical]), False)

        sinfo2 = SInfoT("Zayed", "Sheet", GenT.male, 10.5,
                               SeqADT([DeptT.software, DeptT.chemical]), True)

        sinfo3 = SInfoT("Dom", "Buswoki", GenT.male, 11.0,
                               SeqADT([DeptT.software, DeptT.chemical]), False)

        sinfo4 = SInfoT("Farzad", "Valki", GenT.male, 1.0,
                               SeqADT([DeptT.software, DeptT.chemical]), False)

        sinfo5 = SInfoT("Cat", "Gonzal", GenT.female, 8.4,
                               SeqADT([DeptT.software, DeptT.civil]), True)

        sinfo6 = SInfoT("Pedram", "Yazdinia", GenT.male, 8.0,
                               SeqADT([DeptT.electrical, DeptT.chemical]), False)



        SALst.add("gonzalc", sinfo5)
        SALst.add("yazdiniap", sinfo6)
        SALst.add("buswoki", sinfo3)
        SALst.add("lastf", sinfo1)
        SALst.add("valkarif", sinfo4)
        SALst.add("sheetz", sinfo2)
        SALst.allocate()

        assert AALst.s == [(DeptT.civil, ["lastf"]),(DeptT.chemical, []), (DeptT.electrical, ["yazdiniap"]),
                           (DeptT.mechanical, []), (DeptT.software, ["sheetz", "gonzalc", "buswoki"]),
                           (DeptT.materials, []), (DeptT.engphys, [])]

    def test_allocate_2(self):
        SALst.init()
        SALst.allocate()

        assert AALst.s == [(DeptT.civil, []),(DeptT.chemical, []), (DeptT.electrical, []),
                           (DeptT.mechanical, []), (DeptT.software, []), (DeptT.materials, []),
                           (DeptT.engphys, [])]












