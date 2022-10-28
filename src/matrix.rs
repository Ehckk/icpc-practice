use std::ops::{Index, Add, IndexMut, Mul};


#[derive(Debug, PartialEq)]
pub struct Matrix<const W: usize, const H: usize, T>(pub [ [T; W]; H ] );

pub type IntMatrix<const W: usize, const H: usize> = Matrix<W, H, i32>;

pub type SquareMatrix<const W: usize, T> = Matrix<W, W, T>;

pub trait Zeroed {
    fn zeroed() -> Self;
}

macro_rules! impl_zeroed {
    ($impl_for:ty) => {
        impl<const W: usize, const H: usize> Zeroed for Matrix<W, H, $impl_for> {
            fn zeroed() -> Self {
                Self([ [0 as $impl_for; W]; H ])
            }
        }
    };
}
impl_zeroed!(u16);
impl_zeroed!(i16);
impl_zeroed!(u32);
impl_zeroed!(i32);
impl_zeroed!(u64);
impl_zeroed!(i64);
impl_zeroed!(usize);
impl_zeroed!(isize);
impl_zeroed!(f32);
impl_zeroed!(f64);

impl<const W: usize, const H: usize, T> Matrix<W, H, T> {
    pub const fn from_raw(raw: [[T; W]; H]) -> Self {
        Self(raw)
    }
}

//
// Index into row
//
impl<const W: usize, const H: usize, T> Index<usize> for Matrix<W, H, T> {
    type Output = [T; W];

    fn index(&self, index: usize) -> &Self::Output {
        &self.0[index]
    }
}
impl<const W: usize, const H: usize, T> IndexMut<usize> for Matrix<W, H, T> {

    fn index_mut(&mut self, index: usize) -> &mut Self::Output {
        &mut self.0[index]
    }
}
//
// Index (row, col)
//
impl<const W: usize, const H: usize, T> Index<(usize, usize)> for Matrix<W, H, T> {
    type Output = T;

    fn index(&self, index: (usize, usize)) -> &Self::Output {
        &self.0[index.1][index.0]
    }
}

impl<const W: usize, const H: usize, T> IndexMut<(usize, usize)> for Matrix<W, H, T> {
    fn index_mut(&mut self, index: (usize, usize)) -> &mut Self::Output {
        &mut self.0[index.1][index.0]
    }
}

//
// Addition
//
impl<const W: usize, const H: usize, T> Add<Matrix<W, H, T>> for Matrix<W, H, T> where T: Add + Add<Output = T> + Copy, Self: Zeroed {
    type Output = Matrix<W, H, T>;

    fn add(self, rhs: Matrix<W, H, T>) -> Self::Output {
        let mut m = Self::zeroed();
        for i in 0..W {
            for j in 0..H {
                m[(i, j)] = self[(i,j)] + rhs[(i,j)];
            }
        }
        m
    }
}

// Ref + val
impl<const W: usize, const H: usize, T> Add<&Matrix<W, H, T>> for Matrix<W, H, T> where T: Add + Add<Output = T> + Copy, Self: Zeroed {
    type Output = Matrix<W, H, T>;

    fn add(self, rhs: &Matrix<W, H, T>) -> Self::Output {
        let mut m = Self::zeroed();
        for i in 0..W {
            for j in 0..H {
                m[(i, j)] = self[(i,j)] + rhs[(i,j)];
            }
        }
        m
    }
}
// val + Ref
impl<const W: usize, const H: usize, T> Add<Matrix<W, H, T>> for &Matrix<W, H, T> where T: Add + Add<Output = T> + Copy, Matrix<W, H, T>: Zeroed {
    type Output = Matrix<W, H, T>;

    fn add(self, rhs: Matrix<W, H, T>) -> Self::Output {
        let mut m = Matrix::<W, H, T>::zeroed();
        for i in 0..W {
            for j in 0..H {
                m[(i, j)] = self[(i,j)] + rhs[(i,j)];
            }
        }
        m
    }
}
// Ref + Ref
impl<const W: usize, const H: usize, T> Add<&Matrix<W, H, T>> for &Matrix<W, H, T> where T: Add + Add<Output = T> + Copy, Matrix<W, H, T>: Zeroed {
    type Output = Matrix<W, H, T>;

    fn add(self, rhs: &Matrix<W, H, T>) -> Self::Output {
        let mut m = Matrix::<W, H, T>::zeroed();
        for i in 0..W {
            for j in 0..H {
                m[(i, j)] = self[(i,j)] + rhs[(i,j)];
            }
        }
        m
    }
}

//
// Scalar  Multiplication
//
impl<const W: usize, const H: usize, T> Mul<T> for Matrix<W, H, T> where T: Mul + Mul<Output = T> + Copy, Matrix<W, H, T>: Zeroed {
    type Output = Matrix<W, H, T>;

    fn mul(self, rhs: T) -> Self::Output {
        let mut m = Matrix::<W, H, T>::zeroed();
        for i in 0..W {
            for j in 0..H {
                m[(i, j)] = self[(i,j)] * rhs;
            }
        }
        m
    }
}

impl<const W: usize, const H: usize, T> Mul<T> for &Matrix<W, H, T> where T: Mul + Mul<Output = T> + Copy, Matrix<W, H, T>: Zeroed {
    type Output = Matrix<W, H, T>;

    fn mul(self, rhs: T) -> Self::Output {
        let mut m = Matrix::<W, H, T>::zeroed();
        for i in 0..W {
            for j in 0..H {
                m[(i, j)] = self[(i,j)] * rhs;
            }
        }
        m
    }
}

#[cfg(test)]
mod tests {
    use super::{Matrix, IntMatrix, Zeroed};

    #[test]
    fn build_example_matrix() {
        let mat = IntMatrix::<3, 7>::cardio();
        assert_eq!(
            mat,
            Matrix::from_raw(
                [
                    [1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12],
                    [13,14,15],
                    [16,17,18],
                    [19,20,21],
                ]
            )
        )
    }
    #[test]
    fn add() {
        let m1 = Matrix::<3,3,i32>::zeroed();
        let m2 = Matrix::from_raw([
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ]);
        assert_eq!(
            &m1+&m2,
            m2
        );
        let resulting = 
            IntMatrix::<3,2>::from_raw([
                [1,3,1],
                [1,0,0],
            ]) +
            IntMatrix::<3,2>::from_raw([
                [0,0,5],
                [7,5,0],
            ]);
        assert_eq!(resulting, Matrix::from_raw([
            [1,3,6],
            [8,5,0],
        ]))
    }

    #[test]
    fn test_scalar_mult() {
        let mat = IntMatrix::from_raw([
            [1, 8,-3],
            [4,-2, 5],
        ]);
        assert_eq!(mat * 2,
            IntMatrix::from_raw([
                [2,16,-6],
                [8,-4,10],
            ])
        );
    }
}