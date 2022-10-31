use crate::matrix::{Zeroed, IntMatrix};


fn cardiology<const W: usize, const H: usize>(mat: IntMatrix<W, H>) -> (u32, u32, u32, u32) {
    (0, 0, 0, 0)
}


impl<const W: usize, const H: usize> IntMatrix<W, H> {
    pub fn cardio() -> Self {
        let mut m = Self::zeroed();
        let mut i = 0;
        while i < W*H {
            m.0[i / W][i % W] = i as i32 + 1;
            i += 1;
        }
        m
    }
}