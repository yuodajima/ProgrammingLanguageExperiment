;その1
(define kakeizu
    (read
       (open-input-file "./kakeizu")))

(define get-depth
  (lambda (kakeizu depth)
    (cond ((null? kakeizu) '())
          ((= depth 1) (map car (cdr kakeizu)))
          (else (apply append (map (lambda (l) 
                              (get-depth l (- depth 1))) (cdr kakeizu))))
    )))

(get-depth kakeizu 4)
(get-depth kakeizu 6)

;実行結果
;(家宣 宗尹 家重 宗武)
;(家斎 斎敦 斎匡)

