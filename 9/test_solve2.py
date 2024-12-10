import solve2

class TestSolve2:
    disk: list[solve2.Block] = [(0, 2), (9, 2), (2, 1), (1, 3), (7, 3), (None, 1), (4, 2), (None, 1), (3, 3), (None, 4), (5, 4), (None, 1), (6, 4), (None, 5), (8, 4), (None, 2)]
    
    def test_checksum(self):
        assert solve2.checksum(self.disk) == 2858

    def test_index_block(self):
        assert solve2.index_block(self.disk, 0) == 0
        assert solve2.index_block(self.disk, 9) == 1
        assert solve2.index_block(self.disk, 8) == 14

    def test_remove_block(self):
        disk = [(None, 1), (1, 1), (None, 1)]
        block = solve2.remove_block(disk, 1)
        assert block == (1, 1)
        assert disk == [(None, 3),]

        disk = [(None, 1), (1, 1), (2, 1)]
        block = solve2.remove_block(disk, 1)
        assert block == (1, 1)
        assert disk ==[(None, 2), (2, 1)]

        disk = [(0, 1), (1, 1), (None, 1)]
        block = solve2.remove_block(disk, 1)
        assert block == (1, 1)
        assert disk == [(0, 1), (None, 2)]

        disk = [(0, 1), (1, 1), (2, 1)]
        block = solve2.remove_block(disk, 1)
        assert block == (1, 1)
        assert disk == [(0, 1), (None, 1), (2, 1)]

        disk = [(0, 1), (1, 1), (2, 1)]
        block = solve2.remove_block(disk, 2)
        assert block == (2, 1)
        assert disk == [(0, 1), (1, 1), (None, 1)]

        disk = [(1, 1), (2, 1)]
        block = solve2.remove_block(disk, 1)
        assert block == (1, 1)
        assert disk == [(None, 1), (2, 1)]

        disk = [(1, 1), (None, 1)]
        block = solve2.remove_block(disk, 1)
        assert block == (1, 1)
        assert disk == [(None, 2),]

        disk = [(None, 1), (1, 1)]
        block = solve2.remove_block(disk, 1)
        assert block == (1, 1)
        assert disk == [(None, 2),]