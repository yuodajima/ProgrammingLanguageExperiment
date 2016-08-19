
(define-syntax stream-cons
    (syntax-rules ()
        ((_ x y) (cons x (delay y)))
    ))

(define-syntax stream-car
    (syntax-rules ()
        ((_ x) (car x ))
    ))

(define-syntax stream-cdr
    (syntax-rules ()
        ((_ x) (force (cdr x)))
    ))

(define numbers (lambda ()
  (letrec ((stream
              (lambda (n) (stream-cons n (stream (+ n 1))))
          ))
          (stream 2))))

(define head (lambda (n L)
  (if (<= n 0) '()
      (cons (stream-car L) (head (- n 1) (stream-cdr L)))
      )))

(define prime
  (lambda (num L)
    (if (zero? (modulo (stream-car L) num))
        (prime num (cdr L))
        (append (car L) (prime num (cdr L)))
              )))


(prime 4 (head 100 (numbers)))


