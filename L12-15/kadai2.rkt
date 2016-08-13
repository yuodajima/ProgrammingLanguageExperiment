(define kakeizu
    (read
       (open-input-file "/usr/local/class/scheme/kakeizu")))

(define get-depth
  (lambda (kakeizu depth)
    (cond ((null? kakeizu) '())
          ((= depth 1) (map car (cdr kakeizu)))
          (else get-depth (cdr kakeizu) (- depth 1))
    )))


(get-depth kakeizu 2)

